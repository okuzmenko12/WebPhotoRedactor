from django.contrib import admin

from .models import Plan, UserSubscription, PayPalProduct


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'period']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name', 'price', 'period']


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'plan']
    list_display_links = ['id']
    list_editable = ['plan']
    search_fields = ['id', 'user', 'plan']
    list_filter = ['plan']


@admin.register(PayPalProduct)
class PayPalProductAdmin(admin.ModelAdmin):
    pass
