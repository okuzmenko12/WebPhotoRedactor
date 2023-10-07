import os
import binascii

from enum import Enum


class ImageEnhanceTypes(str, Enum):
    upscale = 'upscale'
    remove_bg = 'remove_bg'
    remove_jpeg_artifacts = 'remove_jpeg_artifacts'


class CounterModelEnhanceFields(str, Enum):
    up_scales_count = 'up_scales_count'
    bg_deletions_count = 'bg_deletions_count'
    jpg_artifacts_deletions_count = 'jpg_artifacts_deletions_count'


def generate_token():
    return binascii.hexlify(os.urandom(16)).decode()
