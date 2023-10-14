from django.urls import path

from .views import (home,
                    StripeWebhookAPIView,
                    StripeConfigAPIView,
                    StripeCheckoutSessionAPIView,
                    CreatePaypalUserSubscriptionAPIView,
                    SubscriptionsAPIVIew,
                    CancelSubscriptionAPIView,
                    CreateUserToBuySubscription,
                    CreatePayPalOrderAPIView,
                    CreateStripeCheckoutSessionAPIView)

urlpatterns = [
    path('all/', SubscriptionsAPIVIew.as_view()),
    path('', home, name='subscriptions-home'),
    path('create_user_for_subscription/', CreateUserToBuySubscription.as_view()),
    path('stripe/config/', StripeConfigAPIView.as_view()),
    path(
        'stripe/create_checkout_session/<int:plan_id>/',
        CreateStripeCheckoutSessionAPIView.as_view()
    ),
    path('stripe/webhook/', StripeWebhookAPIView.as_view()),
    path(
        'paypal/create_user_subscription/',
        CreatePaypalUserSubscriptionAPIView.as_view()
    ),
    path('cancel/<int:subscription_pk>/', CancelSubscriptionAPIView.as_view()),

    path('paypal/create_order/<int:plan_id>/', CreatePayPalOrderAPIView.as_view())
]
