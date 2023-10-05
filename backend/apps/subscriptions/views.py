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

        checkout_session_id = self.create_checkout_session(
            self.request.user.id,
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
    pass


@login_required
def home(request):
    pr = PayPalService()
    user = User.objects.get(email='admin@gmail.com')
    # print(pr.create_user_subscription(user, 'I-PWKHCF6ACC4K'))
    return render(request, 'subscriptions/index.html')


# new
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = settings.BACKEND_DOMAIN
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + '/api/v1/subscriptions/?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + '/cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': 'price_1Nxvl9GesdYQAHLiOYoNpJzb',
                        'quantity': 1,
                    }
                ]
            )
            # print(checkout_session)
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        print(event['data'])
        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new StripeCustomer
        # user = User.objects.get(id=client_reference_id)

        product = stripe.Product.create(
            name='nsd',
            description='lsd'
        )

        price_id = stripe.Price.create(
            unit_amount='1200',
            currency="usd",
            recurring={
                "interval": "month",
                "interval_count": 1
            },
            product=product.id
        )
        # print(product.get('default_price'))

        stripe.Product.modify(
            product.id,
            default_price=price_id.id,
        )
        final_product = stripe.Product.retrieve(product.id)
        print(final_product.default_price)

        # print(final_product.default_price)

        # print(stripe_customer_id)
        # print(stripe_subscription_id)
        # StripeCustomer.objects.create(
        #     user=user,
        #     stripeCustomerId=stripe_customer_id,
        #     stripeSubscriptionId=stripe_subscription_id,
        # )
        # print(user.username + ' just subscribed.')

    return HttpResponse(status=200)
