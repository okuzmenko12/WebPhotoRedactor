import binascii
import os

from django.db import models

from apps.users.models import User


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


class UserFunctionsUsageCounter(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                verbose_name='User',
                                related_name='counter_of_usage')
    up_scales_count = models.IntegerField(
        default=0,
        verbose_name='Up scales count'
    )
    bg_deletions_count = models.IntegerField(
        default=0,
        verbose_name='Background deletions count'
    )
    jpg_artifacts_deletions_count = models.IntegerField(
        default=0,
        verbose_name='JPEG artifacts deletions count'
    )

    class Meta:
        db_table = 'user_functions_usage_counter'
        verbose_name = 'counter'
        verbose_name_plural = 'Usage counters'

    def __str__(self):
        return f'Counter for {self.user}'
