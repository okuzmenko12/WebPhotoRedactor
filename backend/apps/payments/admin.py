from django.contrib import admin

from .models import Plan, Order, ForeignOrder


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(ForeignOrder)
class ForeignOrderAdmin(admin.ModelAdmin):
    pass
