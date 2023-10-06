from typing import Optional

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from apps.picsart.service import PCsService

from .utils import ImageEnhanceTypes
from .serializers import ImageSerializer


class BaseImageAPIView(APIView):
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    psc = PCsService()
    enhance_type: Optional[str] = None

    def post(self, *args, **kwargs):
        image = self.request.data.get('image')
        format_error = self.psc.validate_image_format(image)

        format_error_response = Response({
            'error': format_error
        }, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        if format_error is not None:
            return format_error_response

        serializer = ImageSerializer(data=self.request.data)
        if serializer.is_valid():
            image = serializer.validated_data.get('image')

            enhances_mapping = self.psc.get_enhances_mapping()
            enhance = enhances_mapping[self.enhance_type]
            url_data = enhance(image)
            return Response(url_data)

        return format_error_response


class UpscaleAPIVIew(BaseImageAPIView):
    enhance_type = ImageEnhanceTypes.upscale


class RemoveBGAPIView(BaseImageAPIView):
    enhance_type = ImageEnhanceTypes.remove_bg


class RemoveJPEGArtifactsAPIView(BaseImageAPIView):
    enhance_type = ImageEnhanceTypes.remove_jpeg_artifacts
