from rest_framework import serializers

from .models import PayPalProduct, UserSubscription


class PayPalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayPalProduct
        fields = ['id', 'product_id', 'name', 'description', 'image_url', 'home_url']
        read_only_fields = ['product_id']


class CreateUserSubscriptionSerializer(serializers.Serializer):
    subscription_id = serializers.CharField(required=True,
                                            max_length=250)
