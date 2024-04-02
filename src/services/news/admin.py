from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('', {'fields': ['title', 'description', 'is_active']}),
        ('content', {'fields': ['content', 'image']}),
        ('Dates', {'fields': ['created_at', 'updated_at']}),
    ]