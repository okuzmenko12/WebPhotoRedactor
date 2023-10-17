from django.urls import path
from .views import (UpscaleAPIVIew,
                    RemoveBGAPIView,
                    RemoveJPEGArtifactsAPIView,
                    UpscaleUltraAPIView,
                    UpscaleUltraEnhanceAPIView)

urlpatterns = [
    path('upscale/', UpscaleAPIVIew.as_view()),
    path('upscale/ultra/', UpscaleUltraAPIView.as_view()),
    path('upscale/ultra_enhance/', UpscaleUltraEnhanceAPIView.as_view()),
    path('remove_bg/', RemoveBGAPIView.as_view()),
    path('remove_jpeg_artifacts/', RemoveJPEGArtifactsAPIView.as_view())
]
