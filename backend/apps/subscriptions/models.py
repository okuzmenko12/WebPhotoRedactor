import datetime
from datetime import timedelta
from django.db import models

from apps.users.models import User

from .utils import month_total_days


class Plan(models.Model):
    name = models.CharField(max_length=250,
                            verbose_name='Plan name')
    price = models.IntegerField(verbose_name='Price in $')
    period = models.CharField(
        max_length=150,
        verbose_name='Price per (month, 3 months, 6 months, year etc.)'
    )
    period_in_months = models.IntegerField(verbose_name='Period in months (required)')
    up_scales_count = models.IntegerField(default=100,
                                          verbose_name='Up scales count')
    bg_deletions_count = models.IntegerField(
        default=100,
        verbose_name='Background deletions count')
    jpg_artifacts_deletions_count = models.IntegerField(
        default=100,
        verbose_name='JPEG artifacts deletions count'
    )
    stripe_price_id = models.CharField(max_length=5000,
                                       verbose_name='Stripe price ID',
                                       blank=True,
                                       null=True)
    paypal_plan_id = models.CharField(max_length=350,
                                      verbose_name='PayPal plan Id',
                                      blank=True,
                                      null=True)

    class Meta:
        db_table = 'plans'
        verbose_name = 'plan'
        verbose_name_plural = 'Plans'

    def __str__(self):
        return f'Plan {self.price}$ / {self.period}'


class UserSubscription(models.Model):
    PAYMENT_SERVICE = (
        (1, 'PayPal'),
        (2, 'Stripe')
    )

    plan = models.ForeignKey(Plan,
                             on_delete=models.CASCADE,
                             verbose_name='Subscription')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='User',
                             related_name='subscription')
    started_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Subscription starting date')
    ends_at = models.DateTimeField(verbose_name='Subscription end date',
                                   blank=True,
                                   null=True)
    paypal_subscription_id = models.CharField(
        max_length=450,
        verbose_name='PayPal subscription id',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'users_subscriptions'
        verbose_name = 'subscription'
        verbose_name_plural = 'Users Subscriptions'

    def save(self, *args, **kwargs):
        if not self.ends_at:
            now = datetime.datetime.now()
            self.ends_at = now + timedelta(
                days=month_total_days(now.month, now.year)
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f'User: {self.user.username}. Subscription: {self.subscription}'


class PayPalProduct(models.Model):
    product_id = models.CharField(max_length=350,
                                  verbose_name='PayPal product ID')
    name = models.CharField(max_length=350,
                            verbose_name='PayPal product name')
    description = models.TextField(verbose_name='Description')
    image_url = models.URLField(verbose_name='Image url')
    home_url = models.URLField(verbose_name='Home url')

    class Meta:
        db_table = 'paypal_product'
        verbose_name = 'product'
        verbose_name_plural = 'PayPal Products'

    def __str__(self):
        return f'Product: {self.name}'
