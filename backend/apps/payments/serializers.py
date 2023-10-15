from rest_framework import serializers

from .models import PayPalProduct, UserSubscription, Plan


class PayPalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayPalProduct
        fields = ['id', 'product_id', 'name', 'description', 'image_url', 'home_url']
        read_only_fields = ['product_id']


class CreateUserSubscriptionSerializer(serializers.Serializer):
    subscription_id = serializers.CharField(required=True,
                                            max_length=250)


class CreateUserForSubscriptionMixin(serializers.Serializer):
    full_name = serializers.CharField(max_length=150,
                                      required=False,
                                      label='Full name')
    email = serializers.EmailField(required=True,
                                   label='Email for account creation')


class PlanSerializer(serializers.ModelSerializer):
    period_in_str = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Plan
        fields = ['id', 'name', 'description', 'price',
                  'up_scales_count', 'period_in_months', 'period_in_str',
                  'bg_deletions_count', 'jpg_artifacts_deletions_count',
                  'stripe_price_id', 'paypal_plan_id']

    @staticmethod
    def get_period_in_str(instance: Plan):
        period = str(instance.period_in_months)
        if instance.period_in_months == 1:
            period += ' month'
        elif instance.period_in_months > 1 < 12:
            period += ' months'
        else:
            period += ' year'
        return period
