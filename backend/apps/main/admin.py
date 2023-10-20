from django.contrib import admin

from .models import *


@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(MainFaq)
class MainFaqAdmin(admin.ModelAdmin):
    pass


@admin.register(PricingFaq)
class PricingFaqAdmin(admin.ModelAdmin):
    pass
