from typing import Optional

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .service import (PCsService,
                      get_count_of_enhances_for_field,
                      decrease_count_of_enhances_for_field,
                      IPAddressesUsageCountMixin)
from .utils import ImageEnhanceTypes, CounterModelEnhanceFields
from .serializers import ImageSerializer

from apps.subscriptions.services import UserSubscriptionsService
from apps.users.models import User


class BaseImageAPIView(IPAddressesUsageCountMixin,
                       UserSubscriptionsService,
                       APIView):
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    psc = PCsService()
    enhance_type: Optional[str] = None
    counter_enhance_field: Optional[str] = None

    def post(self, *args, **kwargs):
        image = self.request.data.get('image')
        ip_address = self.request.data.get('ip_address')

        format_error = self.psc.validate_image_format(image)
        reach_limit_resp = Response({
            'error': 'You have reached the usage limit of this feature in this month!'
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

            if self.user_have_active_subscriptions(user):
                self.psc.free_version = False

                if user_count_of_enhances == 0:
                    return reach_limit_resp
                decrease_count_of_enhances_for_field(
                    user,
                    self.counter_enhance_field,
                    1
                )
            else:
                if user_count_of_enhances == 0:

                    error_resp = Response({
                        'error': 'You don\'t have active subscription'
                                 ' and you don\'t have remaining attempts!'
                                 ' To use this feature, subscribe to one of'
                                 ' the plan.'
                    })

                    if ip_address is not None:
                        attempts = self.ip_attempts_for_field(
                            ip_address, self.counter_enhance_field
                        )
                        if attempts >= self.get_features_max_value_of_free_usage():
                            return error_resp
                        self.ip_increase_field_usage_count(ip_address, self.counter_enhance_field)
                    else:
                        return error_resp
                else:
                    self.psc.free_version = False
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
