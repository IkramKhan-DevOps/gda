from django.contrib import admin
from .models import (
    Download, Archive, Type
)


@admin.register(Download)
class DownloadCentreAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'file', 'is_active', 'created_on']
    list_filter = ['is_active', 'created_on']
    search_fields = ['title']
    readonly_fields = ['created_on']


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    search_fields = ['name']
