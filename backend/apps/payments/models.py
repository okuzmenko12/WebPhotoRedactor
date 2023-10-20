from django.db import models

from apps.users.models import User


class Plan(models.Model):
    name = models.CharField(max_length=250,
                            verbose_name='Plan name')
    price = models.IntegerField(verbose_name='Price in $')
    description = models.TextField(max_length=15000,
                                   verbose_name='Description')
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
    stripe_cancel_id = models.CharField(max_length=350,
                                        verbose_name='Stripe cancel ID',
                                        blank=True,
                                        null=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Created at')

    class Meta:
        db_table = 'orders'
        verbose_name = 'order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']

    def __str__(self):
        return f'Order: {self.id}. User: {self.user.username}. Plan: {self.plan.name}'


class ForeignOrder(models.Model):
    ext_id = models.CharField(max_length=250,
                              verbose_name='Internal order ID')
    amount = models.IntegerField(verbose_name='Amount')
    currency = models.CharField(max_length=50,
                                verbose_name='Currency')
    email = models.EmailField(max_length=350,
                              verbose_name='Email',
                              blank=True,
                              null=True)
    description = models.TextField(verbose_name='Description',
                                   blank=True,
                                   null=True)
    success_url = models.URLField(verbose_name='Return success url',
                                  blank=True,
                                  null=True)
    cancel_url = models.URLField(verbose_name='Return cancel url',
                                 blank=True,
                                 null=True)
    notify_url = models.URLField(verbose_name='Notify url',
                                 blank=True,
                                 null=True)
    paypal_order_id = models.CharField(max_length=150,
                                       verbose_name='PayPal order id',
                                       blank=True,
                                       null=True)
    stripe_session_id = models.CharField(max_length=350,
                                         verbose_name='Stripe session id',
                                         blank=True,
                                         null=True)
    stripe_cancel_id = models.CharField(max_length=350,
                                        verbose_name='Stripe cancel ID',
                                        blank=True,
                                        null=True)
    is_ended = models.BooleanField(default=False)

    class Meta:
        db_table = 'foreign_orders'
        verbose_name = 'foreign order'
        verbose_name_plural = 'Foreign Orders'

    def __str__(self):
        return f'Order: {self.ext_id}. Email: {self.email}'
