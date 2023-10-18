from rest_framework import serializers

from .models import Plan, ForeignOrder, Order


class CreateUserForSubscriptionMixin(serializers.Serializer):
    full_name = serializers.CharField(max_length=150,
                                      required=False,
                                      label='Full name')
    email = serializers.EmailField(required=True,
                                   label='Email for account creation')


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'description', 'price',
                  'bg_deletions_count', 'up_scales_count',
                  'jpg_artifacts_deletions_count', 'stripe_price_id']


class ForeignOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignOrder
        fields = '__all__'
        read_only_fields = ['paypal_order_id', 'stripe_session_id', 'is_ended']


class OrderSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'plan', 'status', 'payment_service', 'created_at']
