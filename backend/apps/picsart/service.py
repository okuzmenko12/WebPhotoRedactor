import os
import requests
import cv2
import numpy as np

from PIL import Image

from django.conf import settings

from .models import JPEGArtifactsImages
from .utils import generate_token, ImageEnhanceTypes


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
        os.remove(f'media/{image_token}/{image_name}.{img_format}')
        os.rmdir(f'media/{image_token}')
        return image

    @staticmethod
    def get_upscale_factor(pillow_img):
        factors = [float(2), float(4), float(6), float(8)]
        width, height = pillow_img.size

        for factor in factors:
            if factor * width and factor * height < 16000:
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

    def upscale(self, serializer_img):
        pillow_img = Image.open(serializer_img)
        image = self.get_normalized_image(pillow_img)
        payload = {'upscale_factor': self.get_upscale_factor(pillow_img)}
        response = requests.post(
            self.upscale_url,
            data=payload,
            headers=self.headers,
            files={'image': image}
        )
        return response.json()

    def remove_bg(self, serializer_img):
        pillow_img = Image.open(serializer_img)
        image = self.get_normalized_image(pillow_img)
        payload = {'format': 'PNG',
                   'output_type': 'cutout'}
        response = requests.post(
            self.remove_bg_url,
            data=payload,
            headers=self.headers,
            files={'image': image}
        )
        return response.json()

    def remove_jpeg_artifacts(self, serializer_img):
        image_name: str = serializer_img.name.split('.')[0]
        pillow_img = Image.open(serializer_img)
        byte_image = self.get_normalized_image(pillow_img,
                                               artifacts_removing=True)
        path = self.remove_artifacts(byte_image, image_name)
        return f'{settings.BACK_DOMAIN_URL}/{path}'

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
