from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User

from apps.picsart.models import UserFunctionsUsageCounter


@receiver(post_save, sender=User)
def paypal_product_create(sender, instance: User, created, **kwargs):
    if not created and not UserFunctionsUsageCounter.objects.filter(
            user=instance
    ).exists():
        UserFunctionsUsageCounter.objects.get_or_create(user=instance)
