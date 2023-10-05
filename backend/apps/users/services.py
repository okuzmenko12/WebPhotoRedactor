from .models import User


def get_user_by_id(user_id):
    try:
        user = User.objects.get(user_id)
        return user
    except (Exception,):
        return None
