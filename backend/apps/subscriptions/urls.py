from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='subscriptions-home'),
    path('config/', views.StripeConfigAPIView.as_view()),  # new
    path('create-checkout-session/', views.StripeCheckoutSessionAPIView.as_view()),
    path('webhook/', views.stripe_webhook),
    path('products/', views.PayPalProductAPIView.as_view()),
    path('create/', views.CreateUserSubscriptionAPIView.as_view()),
    path('cancel/<int:subscription_pk>/', views.CancelUserSubscriptionAPIView.as_view()),
]
