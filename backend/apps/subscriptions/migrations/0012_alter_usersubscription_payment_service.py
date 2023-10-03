# Generated by Django 4.2.5 on 2023-10-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0011_usersubscription_payment_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscription',
            name='payment_service',
            field=models.IntegerField(choices=[(1, 'PAYPAL'), (2, 'STRIPE')], verbose_name='Payment service'),
        ),
    ]
