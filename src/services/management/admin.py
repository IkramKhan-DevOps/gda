from django.contrib import admin
from .models import (
    Document, DocumentType
)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'file', 'document_type', 'is_active', 'created_on']
    list_filter = ['document_type', 'is_active']
    search_fields = ['title']
    readonly_fields = ['created_on']
    fieldsets = [
        ('', {'fields': ['title', 'document_type', 'description']}),
        ('File', {'fields': ['file']}),
        ('Status', {'fields': ['is_active', 'created_on']}),
    ]


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_on']
    search_fields = ['name']
