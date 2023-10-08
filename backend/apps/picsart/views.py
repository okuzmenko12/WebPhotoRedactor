from typing import Optional

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .service import PCsService, get_count_of_enhances_for_field, decrease_count_of_enhances_for_field
from .utils import ImageEnhanceTypes, CounterModelEnhanceFields
from .serializers import ImageSerializer

from apps.subscriptions.services import UserSubscriptionsService
from apps.users.models import User


class BaseImageAPIView(UserSubscriptionsService, APIView):
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    psc = PCsService()
    enhance_type: Optional[str] = None
    counter_enhance_field: Optional[str] = None

    def post(self, *args, **kwargs):
        image = self.request.data.get('image')
        format_error = self.psc.validate_image_format(image)

        user: User = self.request.user

        if not user.is_authenticated or user.is_authenticated and not self.user_have_active_subscriptions(
                user
        ):
            # TODO: add method for counting times of using service by IP
            self.psc.free_version = True
        else:
            if self.user_have_active_subscriptions(user):
                self.psc.free_version = False

                if get_count_of_enhances_for_field(user, self.counter_enhance_field) == 0:
                    return Response({
                        'error': 'You have reached the limit!'
                    }, status=status.HTTP_400_BAD_REQUEST)
                decrease_count_of_enhances_for_field(
                    user,
                    self.counter_enhance_field,
                    1
                )

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
    counter_enhance_field = CounterModelEnhanceFields.up_scales_count


class RemoveBGAPIView(BaseImageAPIView):
    enhance_type = ImageEnhanceTypes.remove_bg
    counter_enhance_field = CounterModelEnhanceFields.bg_deletions_count


class RemoveJPEGArtifactsAPIView(BaseImageAPIView):
    enhance_type = ImageEnhanceTypes.remove_jpeg_artifacts
    counter_enhance_field = CounterModelEnhanceFields.jpg_artifacts_deletions_count
