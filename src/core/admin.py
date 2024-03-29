from django.contrib import admin

from .models import (
    Country, Application, NewsLetter
)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'tagline', 'is_active', 'created_on')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'language', 'currency', 'phone_code', 'is_active', 'created_on')


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_active', 'created_on']
    search_fields = ['email']
