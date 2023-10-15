from django.db import models

from apps.users.models import User


class Plan(models.Model):
    name = models.CharField(max_length=250,
                            verbose_name='Plan name')
    price = models.IntegerField(verbose_name='Price in $')
    description = models.TextField(max_length=15000,
                                   verbose_name='Description')
    period_in_months = models.IntegerField(verbose_name='Period in months (required)')
    up_scales_count = models.IntegerField(default=100,
                                          verbose_name='Up scales count')
    bg_deletions_count = models.IntegerField(
        default=100,
        verbose_name='Background deletions count'
    )
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
        return f'Plan {self.price}$'


class Order(models.Model):
    PAYMENT_SERVICES = (
        ('PAYPAL', 'PAYPAL'),
        ('STRIPE', 'STRIPE')
    )
    STATUSES = (
        ('ACTIVE', 'ACTIVE'),
        ('CANCELED', 'CANCELED'),
        ('COMPLETED', 'COMPLETED'),
    )

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='User',
                             related_name='orders')
    plan = models.ForeignKey(Plan,
                             on_delete=models.CASCADE,
                             verbose_name='Plan',
                             related_name='orders')
    status = models.CharField(max_length=45,
                              choices=STATUSES,
                              verbose_name='Order status')
    payment_service = models.CharField(max_length=45,
                                       choices=PAYMENT_SERVICES,
                                       verbose_name='Payment service')
    paypal_order_id = models.CharField(max_length=150,
                                       verbose_name='PayPal order id',
                                       blank=True,
                                       null=True)
    stripe_session_id = models.CharField(max_length=350,
                                         verbose_name='Stripe session id',
                                         blank=True,
                                         null=True)

    class Meta:
        db_table = 'orders'
        verbose_name = 'order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order: {self.id}. User: {self.user.username}. Plan: {self.plan.name}'


class UserSubscription(models.Model):
    PAYMENT_SERVICES = (
        (1, 'PAYPAL'),
        (2, 'STRIPE')
    )
    STATUSES = (
        ('ACTIVE', 'ACTIVE'),
        ('SUSPENDED', 'SUSPENDED'),
        ('CANCELED', 'CANCELED'),
        ('EXPIRED', 'EXPIRED'),
        ('APPROVED', 'APPROVED'),
        ('APPROVAL_PENDING', 'APPROVAL_PENDING')
    )

    plan = models.ForeignKey(Plan,
                             on_delete=models.CASCADE,
                             verbose_name='Plan')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='User',
                             related_name='payments')
    start_time = models.DateTimeField(verbose_name='Subscription starting date',
                                      blank=True,
                                      null=True)
    next_pay_time = models.DateTimeField(verbose_name='Subscription end date',
                                         blank=True,
                                         null=True)
    stripe_subscription_id = models.CharField(max_length=350,
                                              verbose_name='Stripe subscription ID',
                                              blank=True,
                                              null=True)
    paypal_subscription_id = models.CharField(
        max_length=450,
        verbose_name='PayPal subscription id',
        blank=True,
        null=True
    )
    paypal_subscription_cancel_link = models.URLField(
        verbose_name='PayPal subscription cancel link',
        blank=True,
        null=True
    )
    status = models.CharField(max_length=150,
                              verbose_name='Subscription status',
                              choices=STATUSES)
    payment_service = models.IntegerField(verbose_name='Payment service',
                                          choices=PAYMENT_SERVICES)

    class Meta:
        db_table = 'users_subscriptions'
        verbose_name = 'subscription'
        verbose_name_plural = 'Users Subscriptions'

    def __str__(self):
        return f'User: {self.user.username}. Subscription: {self.plan}'


class PayPalProduct(models.Model):
    product_id = models.CharField(max_length=350,
                                  verbose_name='PayPal product ID',
                                  blank=True,
                                  null=True)
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
