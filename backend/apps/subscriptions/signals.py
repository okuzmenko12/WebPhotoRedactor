from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Plan
from .services import PayPalService, StripeMixin


@receiver(post_save, sender=Plan)
def plan_paypal_id_add(sender, instance: Plan, created, **kwargs):
    if not instance.paypal_plan_id:
        pps = PayPalService()
        plan_id = pps.create_plan(
            {
                'name': instance.name,
                'description': instance.description,
                'period_in_months': instance.period_in_months,
                'price': instance.price
            }
        )
        Plan.objects.filter(id=instance.pk).update(paypal_plan_id=plan_id)

    if not instance.stripe_price_id:
        stripe_mixin = StripeMixin()

        price_in_cents = instance.price * 100

        price_id = stripe_mixin.create_product({
            'price': price_in_cents,
            'interval': instance.period_in_months,
            'name': instance.name,
            'description': instance.description
        })
        Plan.objects.filter(id=instance.pk).update(stripe_price_id=price_id)

# @receiver(post_save, sender=StripeProduct)
# def stripe_product_create(sender, instance, created, **kwargs):
#     pass
