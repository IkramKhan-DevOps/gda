from django.contrib import admin
from .models import Projects

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['title', 'description', 'is_active']}),
        ('content', {'fields': ['content', 'image', 'video']}),
        ('Dates', {'fields': ['created_at']}),
    ]
