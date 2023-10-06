from django.urls import path

from .views import (home,
                    StripeWebHookAPIView,
                    StripeConfigAPIView,
                    StripeCheckoutSessionAPIView,
                    CancelUserSubscriptionAPIView,
                    CreateUserSubscriptionAPIView,
                    PayPalProductAPIView,
                    SubscriptionsAPIVIew)

urlpatterns = [
    path('all/', SubscriptionsAPIVIew.as_view()),
    path('', home, name='subscriptions-home'),
    path('config/', StripeConfigAPIView.as_view()),  # new
    path('create-checkout-session/', StripeCheckoutSessionAPIView.as_view()),
    path('webhook/', StripeWebHookAPIView.as_view()),
    path('products/', PayPalProductAPIView.as_view()),
    path('create/', CreateUserSubscriptionAPIView.as_view()),
    path('cancel/<int:subscription_pk>/', CancelUserSubscriptionAPIView.as_view())
]
