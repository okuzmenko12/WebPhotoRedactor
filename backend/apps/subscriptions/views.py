from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Plan, UserSubscription
from .services import (PayPalService,
                       StripeMixin,
                       PaymentService,
                       UserSubscriptionsService,
                       UserCreateForSubscriptionMixin)

from .serializers import (CreateUserSubscriptionSerializer,
                          PlanSerializer,
                          CreateUserForSubscriptionMixin)
from .orders_system import PayPalOrdersMixin, StripePaymentMixin, QuerySetMixin

from apps.users.models import User
from apps.users.services import get_jwt_tokens_for_user
from apps.picsart.service import add_count_of_usage_for_user


class CreateUserToBuySubscription(UserCreateForSubscriptionMixin,
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

        data, error = self.create_order(plan.price)

        if error is not None:
            return Response({
                'error': error
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            data=data,
            status=status.HTTP_201_CREATED
        )


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


class StripeWebhookAPIView(StripePaymentMixin,
                           QuerySetMixin,
                           APIView):

    def post(self, *args, **kwargs):
        payload = self.request.body
        sig_header = self.request.META['HTTP_STRIPE_SIGNATURE']

        print(self.get_payment_data(payload, sig_header))
        return Response(data={'data': True})


class CreatePaypalUserSubscriptionAPIView(UserSubscriptionsService,
                                          PayPalService,
                                          APIView,
                                          PayPalOrdersMixin):
    serializer_class = CreateUserSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        # print(self.create_order(amount=12))
        print(self.capture_order('90Y31590YP0297141'))
        resp = {
            'data': True
        }
        return Response(data=resp, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        if self.user_have_active_subscriptions(self.request.user):
            return Response({
                'error': 'Now you have active subscriptions!'
                         ' At the same time you can have only one.'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        subscription = self.create_user_subscription(
            self.request.user,
            serializer.data.get('subscription_id')
        )

        add_count_of_usage_for_user(self.request.user, subscription.plan)

        return Response({
            'success': f'You successfully bought {subscription.plan.name}!'
        }, status=status.HTTP_201_CREATED)


class StripeConfigAPIView(APIView):

    def get(self, *args, **kwargs):
        config = {'public_key': settings.STRIPE_PUBLISHABLE_KEY}
        return Response(config, status=status.HTTP_200_OK)


class StripeCheckoutSessionAPIView(StripeMixin,
                                   UserSubscriptionsService,
                                   APIView):
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        if self.user_have_active_subscriptions(self.request.user):
            return Response({
                'error': 'Now you have active subscriptions!'
                         ' At the same time you can have only one.'
            }, status=status.HTTP_400_BAD_REQUEST)

        plan_pk = self.kwargs['plan_pk']
        plan = self.get_plan_by_pk(plan_pk)

        if plan is None:
            return Response({
                'error': 'No such plan with provided ID'
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


# class StripeWebHookAPIView(StripeMixin, APIView):
#
#     def post(self, *args, **kwargs):
#         payload = self.request.body
#         sig_header = self.request.META['HTTP_STRIPE_SIGNATURE']
#
#         created = self.create_user_subscription(payload, sig_header)
#
#         if created:
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


class SubscriptionsAPIVIew(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class CancelSubscriptionAPIView(PaymentService, APIView):

    def post(self, *args, **kwargs):
        try:
            subscription = UserSubscription.objects.get(id=self.kwargs['subscription_pk'])
        except (Exception,):
            return Response({
                'error': 'No such subscription with this id!'
            }, status=status.HTTP_400_BAD_REQUEST)

        if subscription.payment_service == 1:
            canceled = self.paypal.cancel_subscription(subscription.id)
        else:
            canceled = self.stripe.cancel_subscription(subscription.id)

        if not canceled:
            return Response({
                'error': 'Something went wrong... Please, try again.'
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'success': 'You successfully canceled this subscription!'
        }, status=status.HTTP_200_OK)


@login_required
def home(request):
    pr = PayPalService()
    user = User.objects.get(email='admin@gmail.com')
    # print(pr.create_user_subscription(user, 'I-PWKHCF6ACC4K'))
    return render(request, 'subscriptions/index.html')
