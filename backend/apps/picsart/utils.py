import os
import binascii
from enum import Enum


class ImageEnhanceTypes(str, Enum):
    upscale = 'upscale'
    remove_bg = 'remove_bg'
    remove_jpeg_artifacts = 'remove_jpeg_artifacts'


def generate_token():
    return binascii.hexlify(os.urandom(16)).decode()
