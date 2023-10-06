from datetime import datetime

import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.users.models import User

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Plan, UserSubscription
from .services import PayPalService, StripeMixin
from .serializers import (PayPalProductSerializer,
                          CreateUserSubscriptionSerializer,
                          StripeCheckoutSerializer)


class PayPalProductAPIView(PayPalService, APIView):
    serializer_class = PayPalProductSerializer

    def post(self, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=self.request.data)
            serializer.is_valid(raise_exception=True)

            product = self.create_product(data=serializer.data)
            serializer = PayPalProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)


class CreateUserSubscriptionAPIView(PayPalService, APIView):
    serializer_class = CreateUserSubscriptionSerializer

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(email='admin@gmail.com')  # USER FOR TEST
        subscription = self.create_user_subscription(user, serializer.data.get('subscription_id'))
        return Response({'STATUS': subscription.status})


class CancelUserSubscriptionAPIView(PayPalService, APIView):

    def post(self, *args, **kwargs):
        sub_pk = self.kwargs['subscription_pk']
        sub_canceled = self.cancel_subscription(sub_pk)

        if not sub_canceled:
            return Response({
                'error': 'The subscription wasn\'t canceled. Please, try again.'  # noqa
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'success': 'The subscription was successfully canceled!'
        }, status=status.HTTP_200_OK)


class StripeConfigAPIView(APIView):

    def get(self, *args, **kwargs):
        config = {'public_key': settings.STRIPE_PUBLISHABLE_KEY}
        return Response(config, status=status.HTTP_200_OK)


class StripeCheckoutSessionAPIView(StripeMixin, APIView):
    serializer_class = StripeCheckoutSerializer

    def get(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        admin = User.objects.get(email='admin@gmail.com')

        checkout_session_id = self.create_checkout_session(
            admin.id,  # self.request.user.id,
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


@login_required
def home(request):
    pr = PayPalService()
    user = User.objects.get(email='admin@gmail.com')
    # print(pr.create_user_subscription(user, 'I-PWKHCF6ACC4K'))
    return render(request, 'subscriptions/index.html')
