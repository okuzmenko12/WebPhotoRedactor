from django.contrib import admin

from .models import Plan, UserSubscription, PayPalProduct


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'period_in_months']
    list_display_links = ['id', 'name']
    list_editable = ['period_in_months']
    search_fields = ['id', 'name', 'price', 'period_in_months']


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
