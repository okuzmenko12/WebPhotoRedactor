from typing import Optional

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .service import (PCsService,
                      get_count_of_enhances_for_field,
                      decrease_count_of_enhances_for_field,
                      IPAddressesUsageCountMixin,
                      UpScalesTypes)
from .utils import ImageEnhanceTypes, CounterModelEnhanceFields
from .serializers import (ImageSerializer,
                          UpscaleSerializer,
                          BgRemoveSerializer,
                          RemoveJPEGArtifactsSerializer)

from apps.users.models import User


class BaseImageAPIView(IPAddressesUsageCountMixin,
                       APIView):
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    psc = PCsService()
    enhance_type: Optional[str] = None
    counter_enhance_field: Optional[str] = None

    @property
    def additional_data(self):
        return {}

    def post(self, *args, **kwargs):
        image = self.request.data.get('image')
        ip_address = self.request.data.get('ip_address')

        if isinstance(image, str):
            return Response({
                'error': 'Something went wrong... Please try again.'
            }, status=status.HTTP_400_BAD_REQUEST)

        format_error = self.psc.validate_image_format(image)
        reach_limit_resp = Response({
            'error': 'You have used all your credits for this feature!'
        }, status=status.HTTP_400_BAD_REQUEST)

        user: User = self.request.user

        if not user.is_authenticated:
            self.psc.free_version = True

            if ip_address is not None:
                attempts = self.ip_attempts_for_field(
                    ip_address, self.counter_enhance_field
                )
                if attempts >= self.get_features_max_value_of_free_usage():
                    return reach_limit_resp
                self.ip_increase_field_usage_count(ip_address, self.counter_enhance_field)

        else:
            user_count_of_enhances = get_count_of_enhances_for_field(
                user,
                self.counter_enhance_field
            )

            if user_count_of_enhances == 0:
                if ip_address is not None:
                    attempts = self.ip_attempts_for_field(
                        ip_address, self.counter_enhance_field
                    )
                    if attempts >= self.get_features_max_value_of_free_usage():
                        return reach_limit_resp
                    self.ip_increase_field_usage_count(ip_address, self.counter_enhance_field)
                else:
                    return reach_limit_resp
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

        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            image = serializer.validated_data.get('image')

            enhances_mapping = self.psc.get_enhances_mapping()
            enhance = enhances_mapping[self.enhance_type]
            url_data: dict = enhance(image, additional_data=self.additional_data)

            if url_data is None:
                return Response({
                    'error': 'Now service is unavailable :( Please wait some time and try again.'
                }, status=status.HTTP_400_BAD_REQUEST)

            if url_data.get('image') is None:
                return Response(url_data, status=status.HTTP_400_BAD_REQUEST)

            url_data.update(
                self.psc.get_image_name_and_format_from_url(
                    url_data.get('image')
                )
            )
            return Response(url_data, status=status.HTTP_200_OK)

        return format_error_response


class UpscaleAPIVIew(BaseImageAPIView):
    serializer_class = UpscaleSerializer
    upscale_type = UpScalesTypes.upscale
    enhance_type = ImageEnhanceTypes.upscale
    counter_enhance_field = CounterModelEnhanceFields.up_scales_count

    @property
    def additional_data(self):
        factor = None
        if self.request.data.get('upscale_factor') != '':
            factor = int(self.request.data.get('upscale_factor'))
        return {
            'upscale_factor': factor,
            'upscale_type': self.upscale_type
        }


class UpscaleUltraAPIView(UpscaleAPIVIew):
    upscale_type = UpScalesTypes.ultra_upscale


class UpscaleUltraEnhanceAPIView(UpscaleAPIVIew):
    upscale_type = UpScalesTypes.ultra_enhance


class RemoveBGAPIView(BaseImageAPIView):
    serializer_class = BgRemoveSerializer
    enhance_type = ImageEnhanceTypes.remove_bg
    counter_enhance_field = CounterModelEnhanceFields.bg_deletions_count

    @property
    def additional_data(self):
        add_fields = ['bg_image', 'bg_image_url', 'bg_color', 'bg_blur', 'output_type']
        additional_dict = {}

        for field in add_fields:
            additional_dict[field] = None
            if field in self.request.data and self.request.data.get(field) != '':
                additional_dict[field] = self.request.data.get(field)
        return additional_dict


class RemoveJPEGArtifactsAPIView(BaseImageAPIView):
    serializer_class = RemoveJPEGArtifactsSerializer
    enhance_type = ImageEnhanceTypes.remove_jpeg_artifacts
    counter_enhance_field = CounterModelEnhanceFields.jpg_artifacts_deletions_count

    # @property
    # def additional_data(self):

