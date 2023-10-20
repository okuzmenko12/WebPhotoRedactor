from django.urls import path

from .views import *

urlpatterns = [
    path('preferences/', PreferenceListAPIView.as_view()),
    path('main_faqs/', MainFaqListAPIView.as_view()),
    path('pricing_faqs/', PricingFaqListAPIView.as_view())
]
