from .models import User

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
