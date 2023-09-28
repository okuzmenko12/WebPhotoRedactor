from django.contrib import admin

from .models import Subscription, UserSubscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'period']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name', 'price', 'period']


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'subscription']
    list_display_links = ['id']
    list_editable = ['subscription']
    search_fields = ['id', 'user', 'subscription']
    list_filter = ['subscription']
