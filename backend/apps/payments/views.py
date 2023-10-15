from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Plan, ForeignOrder

from .serializers import (PlanSerializer,
                          CreateUserForSubscriptionMixin,
                          ForeignOrderSerializer)
from .services import (PayPalOrdersMixin,
                       StripePaymentMixin,
                       QuerySetMixin,
                       UserCreateForPaymentMixin, ForeignOrderMixin)

from apps.users.models import User
from apps.users.services import get_jwt_tokens_for_user


class CreateUserToMakePaymentAPIView(UserCreateForPaymentMixin,
                                     APIView):
    serializer_class = CreateUserForSubscriptionMixin
    mail_with_celery = False

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.data.get('email')
        full_name = serializer.data.get('full_name')
        if not self.check_email_unique(email):
            return Response({
                'error': 'User with provided email is already exists!'
            }, status=status.HTTP_400_BAD_REQUEST)

        user = self.create_user_for_email(email, full_name)

        if user is None:
            return Response({
                'error': 'Something went wrong... Please, try again.'
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'data': get_jwt_tokens_for_user(user)
        }, status=status.HTTP_200_OK)


class CreatePayPalOrderAPIView(PayPalOrdersMixin,
                               QuerySetMixin,
                               APIView):

    def post(self, *args, **kwargs):
        plan_id = self.kwargs.get('plan_id')
        if plan_id is None:
            return Response({
                'error': 'You must provide plan ID'  # noqa
            }, status=status.HTTP_400_BAD_REQUEST)

        plan: Plan = self.get_model_instance_by_id(Plan, plan_id)
        if plan is None:
            return Response({
                'error': 'This plan doesn\'t exists!'  # noqa
            }, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(email='admin@gmail.com')  # self.request.user

        data, error = self.create_order(plan.price)

        if error is not None:
            return Response({
                'error': error
            }, status=status.HTTP_400_BAD_REQUEST)

        self.create_order_in_db({
            'plan': plan,
            'user': user,
            'status': 'ACTIVE',
            'payment_service': 'PAYPAL',
            'paypal_order_id': data.get('order_id')
        })

        return Response(
            data=data,
            status=status.HTTP_201_CREATED
        )


class CompleteOrderByPayPalOrderID(PayPalOrdersMixin,
                                   QuerySetMixin,
                                   APIView):

    def post(self, *args, **kwargs):
        pass


class StripeConfigAPIView(APIView):

    def get(self, *args, **kwargs):
        config = {'public_key': settings.STRIPE_PUBLISHABLE_KEY}
        return Response(config, status=status.HTTP_200_OK)


class CreateStripeCheckoutSessionAPIView(StripePaymentMixin,
                                         QuerySetMixin,
                                         APIView):

    def get(self, *args, **kwargs):
        plan_id = self.kwargs.get('plan_id')
        if plan_id is None:
            return Response({
                'error': 'You must provide plan ID'  # noqa
            }, status=status.HTTP_400_BAD_REQUEST)

        plan: Plan = self.get_model_instance_by_id(Plan, plan_id)
        if plan is None:
            return Response({
                'error': 'This plan doesn\'t exists!'  # noqa
            }, status=status.HTTP_400_BAD_REQUEST)

        checkout_session_id = self.create_checkout_session(
            User.objects.get(email='admin@gmail.com').id,  # self.request.user.id,
            plan
        )
        if checkout_session_id is None:
            return Response({
                'error': 'Something went wrong with payment, please try again!'
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'checkout_session_id': checkout_session_id
        }, status=status.HTTP_201_CREATED)


class CreateStripeForeignCheckoutSessionAPIView(ForeignOrderMixin,
                                                APIView):
    serializer_class = ForeignOrderSerializer
    foreign_order = True

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        order: ForeignOrder = serializer.save()

        checkout_session_id = self.create_checkout_session(
            client_id=order.email,
            foreign_order=order
        )
        if checkout_session_id is None:
            return Response({
                'error': 'Something went wrong with payment, please try again!'
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'checkout_session_id': checkout_session_id
        }, status=status.HTTP_201_CREATED)


class StripeWebhookAPIView(StripePaymentMixin,
                           QuerySetMixin,
                           APIView):

    def post(self, *args, **kwargs):
        payload = self.request.body
        sig_header = self.request.META['HTTP_STRIPE_SIGNATURE']
        self.complete_payment(payload, sig_header)
        return Response(data={'data': True})


class PlansAPIVIew(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class CreatePayPalForeignOrderAPIView(PayPalOrdersMixin,
                                      APIView):
    serializer_class = ForeignOrderSerializer
    foreign_order = True

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        order: ForeignOrder = serializer.save()

        data, error = self.create_order(order.amount)

        if error is not None:
            return Response({
                'error': error
            }, status=status.HTTP_400_BAD_REQUEST)

        order.paypal_order_id = data.get('order_id')
        order.save()

        return Response(
            data=data,
            status=status.HTTP_201_CREATED
        )


class CompleteForeignOrderByPayPalOrderID(ForeignOrderMixin,
                                          APIView):
    foreign_order = True

    def post(self, *args, **kwargs):
        order_id = self.kwargs.get('order_id')

        if order_id is None:
            return Response({
                'error': 'Order ID must be provided!'
            }, status=status.HTTP_400_BAD_REQUEST)

        data, error = self.foreign_paypal_capture(order_id)

        if error is not None:
            return Response({
                'error': error
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status.HTTP_200_OK)


@login_required
def home(request):
    user = User.objects.get(email='admin@gmail.com')
    # print(pr.create_user_subscription(user, 'I-PWKHCF6ACC4K'))
    return render(request, 'payments/index.html')
