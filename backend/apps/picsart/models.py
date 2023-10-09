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


class AbstractFunctionsUsageCounter(models.Model):
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
        abstract = True
        verbose_name = 'counter'


class UserFunctionsUsageCounter(AbstractFunctionsUsageCounter):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                verbose_name='User',
                                related_name='counter_of_usage')

    class Meta:
        db_table = 'user_functions_usage_counter'
        verbose_name_plural = 'Usage counters (Authenticated users)'

    def __str__(self):
        return f'Counter for: {self.user.username}'


class AnonymousUserFunctionsUsageCounter(AbstractFunctionsUsageCounter):
    ip_address = models.GenericIPAddressField(max_length=25,
                                              verbose_name='IP Address',
                                              unique=True)

    class Meta:
        db_table = 'ip_functions_usage_counter'
        verbose_name_plural = 'Usage counters (Anonymous users)'

    def __str__(self):
        return f'Counter for: {self.ip_address}'


class FreeEnhancesLimit(models.Model):
    limit = models.IntegerField(default=5,
                                verbose_name='Limit for free using of all features')

    class Meta:
        db_table = 'free_enhances_limit'
        verbose_name = 'limit'
        verbose_name_plural = 'Free enhances limit'

    def __str__(self):
        return f'Limit: {str(self.limit)}'
