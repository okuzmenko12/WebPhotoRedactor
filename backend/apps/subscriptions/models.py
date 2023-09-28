import datetime
from datetime import timedelta
from django.db import models

from apps.users.models import User

from .utils import month_total_days


class Subscription(models.Model):
    name = models.CharField(max_length=250,
                            verbose_name='Plan/Subscription name')
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

    class Meta:
        db_table = 'subscriptions'
        verbose_name = 'subscription'
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return f'Subscription {self.price}$ / {self.period}'


class UserSubscription(models.Model):
    subscription = models.ForeignKey(Subscription,
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
