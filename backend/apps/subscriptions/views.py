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

from .services import PayPalService
from .serializers import PayPalProductSerializer


class StripeConfigAPIView(PayPalService, APIView):

    def get(self, *args, **kwargs):
        config = {'public_key': settings.STRIPE_PUBLISHABLE_KEY}
        return Response(config, status=status.HTTP_200_OK)


class StripeCheckoutSessionAPIView(APIView):

    def post(self, *args, **kwargs):
        pass


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


@login_required
def home(request):
    return render(request, 'subscriptions/index.html')


# new
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        pr = PayPalService()
        product = pr.create_product(
            {
                'name': 'Upscale',
                'description': 'upscale site',
                'image_url': 'https://example.com',
                'home_url': 'https://example.com'
            }
        )
        print(product)
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

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

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        print(stripe_customer_id)
        print(stripe_subscription_id)
        # StripeCustomer.objects.create(
        #     user=user,
        #     stripeCustomerId=stripe_customer_id,
        #     stripeSubscriptionId=stripe_subscription_id,
        # )
        print(user.username + ' just subscribed.')

    return HttpResponse(status=200)
