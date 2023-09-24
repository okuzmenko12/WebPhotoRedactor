from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils.text import slugify

from .manager import UserManager


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(max_length=254,
                              unique=True,
                              db_index=True,
                              verbose_name='Email',
                              blank=False,
                              null=False)
    username = models.CharField(max_length=250,
                                verbose_name='Username',
                                unique=True,
                                blank=True,
                                null=False)
    full_name = models.CharField(max_length=250,
                                 verbose_name='Full name',
                                 blank=True)
    is_staff = models.BooleanField(verbose_name='Staff status', default=False)
    is_superuser = models.BooleanField(verbose_name='Superuser status', default=False)
    is_active = models.BooleanField(verbose_name='User activated', default=True)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name='Last login', null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='Date joined', auto_now_add=True)
    slug = models.SlugField(unique=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.email}'

    @classmethod
    def slugify_username(cls, username: str) -> str:
        """Returns 'username' for slug."""
        return slugify(username)

    def save(self, *args, **kwargs):
        if self._state.adding and (User.objects.filter(username=self.username).exists()
                                   or not self.username):
            if not self.full_name:
                self.full_name = 'user'
            self.username = User.objects.generate_username(self.email)
        if self._state.adding and not self.slug:
            self.slug = self.slugify_username(self.username)
        super().save(*args, **kwargs)
