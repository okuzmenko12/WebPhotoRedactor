from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    ip_address_or_token = serializers.CharField(required=True,
                                                label='IP Address or Token',
                                                max_length=250)
    image = serializers.ImageField()


class UpscaleSerializer(ImageSerializer):
    upscale_factor = serializers.IntegerField(required=False,
                                              label='Upscale factor')


class BgRemoveSerializer(ImageSerializer):
    OUTPUT_TYPE_CHOICES = (
        ('cutout', 'cutout'),
        ('mask', 'mask')
    )

    bg_image = serializers.ImageField(required=False,
                                      label='Bg image')
    bg_image_url = serializers.URLField(required=False,
                                        label='Bg image URL')
    bg_color = serializers.CharField(max_length=250,
                                     required=False,
                                     label='Bg color')
    bg_blur = serializers.IntegerField(min_value=0,
                                       required=False,
                                       max_value=100)
    output_type = serializers.ChoiceField(choices=OUTPUT_TYPE_CHOICES,
                                          default='cutout')


class RemoveJPEGArtifactsSerializer(ImageSerializer):
    STRENGTH_CHOICES = (
        ('normal', 'normal'),
        ('high', 'high'),
        ('maximal', 'maximal')
    )

    strength = serializers.ChoiceField(choices=STRENGTH_CHOICES,
                                       label='Artifacts removing choices',
                                       default=STRENGTH_CHOICES)
