from rest_framework.generics import ListAPIView

from .models import *
from .serializers import PreferenceSerializer, MainFaqSerializer, PricingFaqSerializer


class PreferenceListAPIView(ListAPIView):
    serializer_class = PreferenceSerializer
    queryset = Preference.objects.all()


class MainFaqListAPIView(ListAPIView):
    serializer_class = MainFaqSerializer
    queryset = MainFaq.objects.all()


class PricingFaqListAPIView(ListAPIView):
    serializer_class = PricingFaqSerializer
    queryset = PricingFaq.objects.all()
