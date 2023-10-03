from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='subscriptions-home'),
    path('config/', views.stripe_config),  # new
    path('create-checkout-session/', views.create_checkout_session),
    path('webhook/', views.stripe_webhook),
    path('products/', views.PayPalProductAPIView.as_view()),
    path('create/', views.CreateUserSubscriptionAPIView.as_view()),
    path('cancel/<int:subscription_pk>/', views.CancelUserSubscriptionAPIView.as_view())
]
