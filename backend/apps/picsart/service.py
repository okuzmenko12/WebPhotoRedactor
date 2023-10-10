import os
from io import BytesIO

from urllib.parse import urlparse
from urllib.request import urlopen, Request

import requests
import cv2
import numpy as np

from PIL import Image, ImageDraw

from django.conf import settings

from .models import (JPEGArtifactsImages,
                     AnonymousUserFunctionsUsageCounter,
                     FreeEnhancesLimit)
from .utils import generate_token, ImageEnhanceTypes, CounterModelEnhanceFields
from apps.subscriptions.models import Plan
from apps.users.models import User


class RequestContextMixin:

    @property
    def upscale_url(self):
        return 'https://api.picsart.io/tools/1.0/upscale/enhance'

    @property
    def remove_bg_url(self):
        return 'https://api.picsart.io/tools/1.0/removebg'

    @property
    def headers(self):
        return {
            "accept": "application/json",
            "x-picsart-api-key": settings.PICSART_API_KEY
        }


class ImageFilesMixin:

    @staticmethod
    def _byte_image(pillow_img, img_format: str, image_name=None):
        if image_name is None:
            image_name = 'temp_image'
        image_token = generate_token()
        if not os.path.exists('media'):
            os.makedirs('media', exist_ok=True)
        os.mkdir(f'media/{image_token}')
        pillow_img.save(f'media/{image_token}/{image_name}.{img_format}')
        image = open(f'media/{image_token}/{image_name}.{img_format}', 'rb')

        return {
            'image': image,
            'image_token': image_token,
            'image_name': image_name,
            'img_format': img_format
        }

    @staticmethod
    def get_upscale_factor(pillow_img):
        factors = [float(2), float(4), float(6), float(8)]
        width, height = pillow_img.size

        for factor in factors:
            if factor * width < 16000 and factor * height < 16000:
                return factor
        return None

    @staticmethod
    def get_image_params(pillow_img) -> dict:
        format_mapping = {
            'PNG': {'format': 'png', 'rotate': 0},
            'MPO': {'format': 'jpg', 'rotate': -90},
            'JPEG': {'format': 'jpeg', 'rotate': 0},
            'TIFF': {'format': 'tiff', 'rotate': 0},
            'TGA': {'format': 'tga', 'rotate': 0},
        }
        format_img = 'png'
        rotate = 0
        if pillow_img.format in format_mapping.keys():
            img_params = format_mapping[pillow_img.format]
            format_img = img_params['format']
            rotate = img_params['rotate']
        return {
            'format': format_img,
            'rotate': rotate
        }

    def get_normalized_image(
            self,
            pillow_img,
            artifacts_removing=False,
            image_name=None
    ):
        params = self.get_image_params(pillow_img)
        image_format = params.get('format') if not artifacts_removing else 'png'
        rotated_img = pillow_img.rotate(params.get('rotate'), expand=True)
        byte_image = self._byte_image(rotated_img, image_format, image_name)
        return byte_image


class JPEGArtifactsRemoverMixin:

    @staticmethod
    def remove_artifacts(byte_image, image_name):
        image_array = np.frombuffer(byte_image.read(), dtype=np.uint8)
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        dsd_image = cv2.fastNlMeansDenoisingColored(
            img,
            None,
            10,
            10,
            7,
            21
        )
        _, processed_image = cv2.imencode('.jpg', dsd_image)

        if not os.path.exists('media'):
            os.makedirs('media', exist_ok=True)

        image_token = generate_token()
        os.mkdir(f'media/{image_token}')

        media_path = os.path.join('media', f'{image_token}/{image_name}.jpg')

        with open(media_path, 'wb') as media_file:
            media_file.write(processed_image.tobytes())

        JPEGArtifactsImages.objects.create(image_token=image_token)

        return media_path


class PCsService(RequestContextMixin,
                 ImageFilesMixin,
                 JPEGArtifactsRemoverMixin):
    free_version = True

    @staticmethod
    def _add_watermark_to_url_image(image_url):
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) '
                          'Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}

        req = Request(image_url, headers=hdr)

        response = urlopen(req)
        image_data = BytesIO(response.read())
        image = Image.open(image_data)

        watermark_img = Image.open('watermark/watermark.png')
        width, height = image.size
        watermark_img = watermark_img.resize((width, height), Image.Resampling.LANCZOS)

        image.paste(watermark_img, (0, 0), watermark_img)

        if not os.path.exists('media'):
            os.makedirs('media', exist_ok=True)
        image_token = generate_token()
        os.mkdir(f'media/{image_token}')

        parsed_url = urlparse(image_url)
        image_name = os.path.basename(parsed_url.path).split('.')[0]
        media_path = os.path.join('media', f'{image_token}/{image_name}.png')

        image.save(media_path)

        return media_path

    def get_pillow_img(self, serializer_img, for_bg_remove=False):
        image = Image.open(serializer_img)
        if self.free_version and not for_bg_remove:
            ImageDraw.Draw(image)
            watermark_img = Image.open('watermark/watermark.png')
            width, height = image.size
            watermark_img = watermark_img.resize((width, height), Image.Resampling.LANCZOS)

            position1 = (50, 50)
            image.paste(watermark_img, position1, watermark_img)

        return image

    @staticmethod
    def get_normalized_data_from_api_service(
            response_data
    ) -> dict | None:
        data = None
        if response_data.get('status') == 'success':
            resp_data = response_data.get('data')
            data = {
                'image': resp_data.get('url')
            }
        return data

    def upscale(self, serializer_img):
        pillow_img = self.get_pillow_img(serializer_img)
        image_dict = self.get_normalized_image(pillow_img)
        image = image_dict.get('image')

        payload = {'upscale_factor': self.get_upscale_factor(pillow_img)}
        response = requests.post(
            self.upscale_url,
            data=payload,
            headers=self.headers,
            files={'image': image}
        )
        image.close()
        os.remove(f'media/{image_dict["image_token"]}/{image_dict["image_name"]}.{image_dict["img_format"]}')
        os.rmdir(f'media/{image_dict["image_token"]}')
        data = self.get_normalized_data_from_api_service(response.json())
        return data

    def remove_bg(self, serializer_img):
        pillow_img = self.get_pillow_img(serializer_img, for_bg_remove=True)
        image_dict = self.get_normalized_image(pillow_img)
        image = image_dict.get('image')

        payload = {'format': 'PNG',
                   'output_type': 'cutout'}
        response = requests.post(
            self.remove_bg_url,
            data=payload,
            headers=self.headers,
            files={'image': image}
        )

        response_data = response.json()

        image.close()
        os.remove(f'media/{image_dict["image_token"]}/{image_dict["image_name"]}.{image_dict["img_format"]}')
        os.rmdir(f'media/{image_dict["image_token"]}')

        data = self.get_normalized_data_from_api_service(response.json())

        if response.status_code == 200 and self.free_version:
            image_url = response_data.get('data').get('url')
            image_path = self._add_watermark_to_url_image(image_url)
            return {
                'image': f'{settings.BACK_DOMAIN_URL}/{image_path}'
            }
        return data

    def remove_jpeg_artifacts(self, serializer_img):
        image_name: str = serializer_img.name.split('.')[0]
        pillow_img = self.get_pillow_img(serializer_img)
        image_dict = self.get_normalized_image(pillow_img,
                                               artifacts_removing=True)
        byte_image = image_dict.get('image')

        path = self.remove_artifacts(byte_image, image_name)

        byte_image.close()
        os.remove(f'media/{image_dict["image_token"]}/{image_dict["image_name"]}.{image_dict["img_format"]}')
        os.rmdir(f'media/{image_dict["image_token"]}')

        return {
            'image': f'{settings.BACK_DOMAIN_URL}/{path}'
        }

    @classmethod
    def validate_image_format(cls, serializer_img):
        image_format_error = ('Unsupported file format. Please upload an '
                              'image (jpg, jpeg, png, tiff, tga).')
        if serializer_img is None:
            return image_format_error
        valid_formats = ['png', 'jpg', 'jpeg', 'tiff', 'tga']
        if serializer_img.name.split('.')[-1] not in valid_formats:
            return image_format_error
        return None

    def get_enhances_mapping(self):
        return {
            ImageEnhanceTypes.upscale: self.upscale,
            ImageEnhanceTypes.remove_bg: self.remove_bg,
            ImageEnhanceTypes.remove_jpeg_artifacts: self.remove_jpeg_artifacts
        }


class IPAddressesUsageCountMixin:

    @staticmethod
    def get_features_max_value_of_free_usage():
        default_limit = 5
        limit_instance = FreeEnhancesLimit.objects.first()
        if limit_instance is None:
            return default_limit
        return limit_instance.limit

    @staticmethod
    def get_or_create_ip(ip_address):
        if ip_address is not None:
            model_objects = AnonymousUserFunctionsUsageCounter.objects
            data = {
                'ip_address': ip_address
            }
            if not model_objects.filter(
                    **data
            ).exists():
                return model_objects.create(
                    **data
                )
            return model_objects.get(
                **data
            )
        return None

    def ip_attempts_for_field(
            self,
            ip_address,
            enhance_field
    ):
        ip = self.get_or_create_ip(ip_address)
        field_value_count = getattr(ip, enhance_field)
        return field_value_count

    def ip_increase_field_usage_count(
            self,
            ip_address,
            enhance_field
    ):
        ip = self.get_or_create_ip(ip_address)
        old_value = getattr(ip, enhance_field)
        new_value = old_value + 1
        setattr(ip, enhance_field, new_value)
        ip.save()


def get_count_of_enhances_for_field(user, counter_field):
    counter_of_usage = user.counter_of_usage
    count = getattr(counter_of_usage, counter_field)
    return count


def decrease_count_of_enhances_for_field(
        user,
        counter_field,
        value
):
    counter_of_usage = user.counter_of_usage
    old_value = getattr(counter_of_usage, counter_field)
    if old_value != 0:
        new_value = old_value - value
    else:
        new_value = 0
    setattr(counter_of_usage, counter_field, new_value)
    counter_of_usage.save()


def add_count_of_usage_for_user(user: User, plan: Plan):
    counter_of_usage = user.counter_of_usage

    counter_of_usage.up_scales_count += plan.up_scales_count
    counter_of_usage.bg_deletions_count += plan.bg_deletions_count
    counter_of_usage.jpg_artifacts_deletions_count += plan.jpg_artifacts_deletions_count
    counter_of_usage.save()
