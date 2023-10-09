from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    ip_address = serializers.IPAddressField(required=False,
                                            label='IP Address (not required)',
                                            max_length=25)
    image = serializers.ImageField()
