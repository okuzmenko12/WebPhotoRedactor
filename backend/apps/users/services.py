import binascii
import os

from .models import User

from apps.picsart.models import (AnonymousUserFunctionsUsageCounter,
                                 UserFunctionsUsageCounter,
                                 FreeEnhancesLimit)

from rest_framework_simplejwt.tokens import RefreshToken


def get_user_by_id(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user
    except (Exception,):
        return None


def get_jwt_tokens_for_user(user: User) -> dict:
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


def get_or_create_usage_counter_for_ip_or_token(user_ip_or_token):
    usage_counter, _ = AnonymousUserFunctionsUsageCounter.objects.get_or_create(
        ip_address_or_token=user_ip_or_token
    )
    return usage_counter


def get_credits_for_ip_or_token(user_ip_or_token):
    credits_left_dict = {}
    counter_fields = ['up_scales_count', 'bg_deletions_count', 'jpg_artifacts_deletions_count']
    usage_counter = get_or_create_usage_counter_for_ip_or_token(user_ip_or_token)

    free_limit = 5
    if FreeEnhancesLimit.objects.count() > 0:
        free_limit = FreeEnhancesLimit.objects.first().limit

    for field in counter_fields:
        field_value = getattr(usage_counter, field)
        if field_value != 0:
            final_value = free_limit - field_value
        else:
            final_value = 0
        credits_left_dict[field] = final_value
    return credits_left_dict


def get_user_credits(
        user_ip_or_token,
        is_authenticated,
        user_id=None
):
    credits_left_dict = {
        'free_credits': {},
        'paid_credits': {}
    }
    counter_fields = [
        'up_scales_count',
        'bg_deletions_count',
        'jpg_artifacts_deletions_count'
    ]

    if not is_authenticated:
        ip_credits = get_credits_for_ip_or_token(user_ip_or_token)
        for field, value in ip_credits.items():
            credits_left_dict['free_credits'][field] = value
            credits_left_dict['paid_credits'][field] = 0
    else:
        usage_counter = UserFunctionsUsageCounter.objects.get(user_id=user_id)
        for field in counter_fields:
            field_value = getattr(usage_counter, field)
            credits_left_dict['paid_credits'][field] = field_value

        ip_credits = get_credits_for_ip_or_token(user_ip_or_token)
        for field, value in ip_credits.items():
            credits_left_dict['free_credits'][field] = value

    return credits_left_dict


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return {
        'ip': ip,
        'addr': request.META.get('REMOTE_ADDR'),
        'x_forwarded_for': x_forwarded_for
    }


class NotAuthenticatedUsersTokensMixin:

    @classmethod
    def generate_token(cls):
        return binascii.hexlify(os.urandom(32)).decode()

    def create_token(self):
        return self.generate_token()
