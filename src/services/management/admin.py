from django.contrib import admin
from .models import (
    Document, DocumentType, Department
)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'file', 'document_type', 'is_active', 'created_at']
    list_filter = ['document_type', 'is_active']
    search_fields = ['title']
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['title', 'document_type', 'description']}),
        ('File', {'fields': ['file']}),
        ('Status', {'fields': ['is_active', 'created_at']}),
    ]


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name']
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['name', 'description', 'rank', 'image', 'message', 'is_active']}),
        ('Dates', {'fields': ['created_at']}),
    ]