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
    path('config/', StripeConfigAPIView.as_view()),
    path('create-checkout-session/', StripeCheckoutSessionAPIView.as_view()),
    path('webhook/', StripeWebHookAPIView.as_view()),
    path('create/', CreatePaypalUserSubscriptionAPIView.as_view()),
    path('cancel/<int:subscription_pk>/', CancelSubscriptionAPIView.as_view())
]
