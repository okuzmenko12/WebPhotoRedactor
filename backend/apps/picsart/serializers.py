from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    ip_address = serializers.IPAddressField(required=True,
                                            label='IP Address',
                                            max_length=25)
    image = serializers.ImageField()
