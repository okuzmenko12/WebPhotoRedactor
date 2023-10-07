from django.contrib import admin

from .models import UserFunctionsUsageCounter


@admin.register(UserFunctionsUsageCounter)
class UserFunctionsUsageCounterAdmin(admin.ModelAdmin):
    pass
