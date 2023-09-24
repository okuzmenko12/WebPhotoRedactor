from django.urls import path
from .views import UpscaleAPIVIew, RemoveBGAPIView, RemoveJPEGArtifactsAPIView

urlpatterns = [
    path('upscale/', UpscaleAPIVIew.as_view()),
    path('remove_bg/', RemoveBGAPIView.as_view()),
    path('remove_jpeg_artifacts/', RemoveJPEGArtifactsAPIView.as_view())
]
