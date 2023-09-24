import binascii
import os

from django.db import models


class JPEGArtifactsImages(models.Model):
    image_token = models.CharField(max_length=250,
                                   verbose_name='Image token')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'jpeg_artifacts_images'
        verbose_name = 'jpeg artifact image'
        verbose_name_plural = 'JPEG Artifacts images'

    def __str__(self):
        return f'Image token: {self.image_token}'

    @classmethod
    def generate_token(cls):
        return binascii.hexlify(os.urandom(16)).decode()
