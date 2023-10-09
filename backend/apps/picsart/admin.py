from django.contrib import admin

from .models import (UserFunctionsUsageCounter,
                     AnonymousUserFunctionsUsageCounter,
                     FreeEnhancesLimit)


@admin.register(UserFunctionsUsageCounter)
class UserFunctionsUsageCounterAdmin(admin.ModelAdmin):
    pass


@admin.register(AnonymousUserFunctionsUsageCounter)
class AnonymousUserFunctionsUsageCounterAdmin(admin.ModelAdmin):
    pass


@admin.register(FreeEnhancesLimit)
class AnonymousUserEnhancesLimitAdmin(admin.ModelAdmin):
    pass
