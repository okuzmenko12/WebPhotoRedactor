from django.urls import path

from .views import (home,
                    StripeWebhookAPIView,
                    StripeConfigAPIView,
                    CreateStripeCheckoutSessionAPIView,
                    CreateUserToMakePaymentAPIView,
                    CreatePayPalOrderAPIView,
                    PlansAPIVIew,
                    CreatePayPalForeignOrderAPIView,
                    CompleteForeignOrderByPayPalOrderID,
                    CreateStripeForeignCheckoutSessionAPIView)

urlpatterns = [
    path('all/', PlansAPIVIew.as_view()),
    path('', home, name='payments-home'),
    path('create_user_for_subscription/',
         CreateUserToMakePaymentAPIView.as_view()),
    path('stripe/config/', StripeConfigAPIView.as_view()),
    path('stripe/webhook/', StripeWebhookAPIView.as_view()),
    path('stripe/create_checkout_session/<int:plan_id>/',
         CreateStripeCheckoutSessionAPIView.as_view()),
    path('stripe/foreign/create_checkout_session/', CreateStripeForeignCheckoutSessionAPIView.as_view()),
    path('paypal/create_order/<int:plan_id>/', CreatePayPalOrderAPIView.as_view()),
    path('paypal/foreign/create_order/', CreatePayPalForeignOrderAPIView.as_view()),
    path('paypal/foreign/complete_order/<str:order_id>/', CompleteForeignOrderByPayPalOrderID.as_view())
]
