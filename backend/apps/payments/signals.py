from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Plan

from .services import StripePaymentMixin


@receiver(post_save, sender=Plan)
def plan_paypal_id_add(sender, instance: Plan, created, **kwargs):
    if not instance.stripe_price_id:
        stripe_mixin = StripePaymentMixin()

        price_in_cents = instance.price * 100

        price_id = stripe_mixin.create_product({
            'price': price_in_cents,
            'name': instance.name,
            'description': instance.description
        })
        Plan.objects.filter(id=instance.pk).update(stripe_price_id=price_id)
