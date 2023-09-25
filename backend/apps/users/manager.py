from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):

    def generate_username(self, email: str):
        username = '@' + email.split('@')[0]
        if not self.filter(username=username).exists():
            return username
        suffix = 1
        while self.filter(username=username + str(suffix)).exists():
            suffix += 1
        return username + str(suffix)

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        extra_fields['username'] = self.generate_username(email)
        user = self.model(
            email=email,
            is_active=True,
            date_joined=timezone.now(),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        return self._create_user(email, password, **extra_fields)
