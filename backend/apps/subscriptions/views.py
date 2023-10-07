from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.users.models import User

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Plan, UserSubscription
from .services import (PayPalService,
                       StripeMixin,
                       PaymentService,
                       UserSubscriptionsService)
from .serializers import (CreateUserSubscriptionSerializer,
                          StripeCheckoutSerializer,
                          PlanSerializer)


class CreatePaypalUserSubscriptionAPIView(UserSubscriptionsService,
                                          PayPalService,
                                          APIView):
    serializer_class = CreateUserSubscriptionSerializer
    permission_classes = [IsAuthenticated]

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
    serializer_class = StripeCheckoutSerializer
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

        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        checkout_session_id = self.create_checkout_session(
            self.request.user.id,
            plan,
            serializer.data.get('success_url'),
            serializer.data.get('cancel_url')
        )
        if checkout_session_id is None:
            return Response({
                'error': 'Something went wrong with payment, please try again!'
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'checkout_session_id': checkout_session_id
        }, status=status.HTTP_201_CREATED)


class StripeWebHookAPIView(StripeMixin, APIView):

    def post(self, *args, **kwargs):
        payload = self.request.body
        sig_header = self.request.META['HTTP_STRIPE_SIGNATURE']

        created = self.create_user_subscription(payload, sig_header)

        if created:
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


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
