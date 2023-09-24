from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'full_name']
    list_display_links = ['id', 'email']
    search_fields = ['id', 'username', 'email', 'full_name']

    fieldsets = (
        ('User info', {'fields': ('full_name', 'username', 'email')}),
        ('Permissions', {'fields': (
            'is_staff',
            'is_superuser',
            'is_admin',
        )}),
        ('Additional info', {'fields': ('is_active', 'last_login', 'date_joined')})
    )
    readonly_fields = ['date_joined']
