from django.urls import path

from .views import (home,
                    StripeWebHookAPIView,
                    StripeConfigAPIView,
                    StripeCheckoutSessionAPIView,
                    CreatePaypalUserSubscriptionAPIView,
                    SubscriptionsAPIVIew,
                    CancelSubscriptionAPIView)

urlpatterns = [
    path('all/', SubscriptionsAPIVIew.as_view()),
    path('', home, name='subscriptions-home'),
    path('stripe/config/', StripeConfigAPIView.as_view()),
    path(
        'stripe/create_checkout_session/<int:plan_pk>/',
        StripeCheckoutSessionAPIView.as_view()
    ),
    path('stripe/webhook/', StripeWebHookAPIView.as_view()),
    path(
        'paypal/create_user_subscription/',
        CreatePaypalUserSubscriptionAPIView.as_view()
    ),
    path('cancel/<int:subscription_pk>/', CancelSubscriptionAPIView.as_view())
]
