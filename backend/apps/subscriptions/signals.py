from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Plan
from .services import PayPalService


@receiver(post_save, sender=Plan)
def plan_paypal_id_add(sender, instance, created, **kwargs):
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
