from django.contrib import admin

from .models import ServiceProvider


@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'contact_phone', 'contact_email', 'address')


