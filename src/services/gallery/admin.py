from django.contrib import admin
from .models import (
    Image, Video
)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['title', 'description', 'image', 'is_active']}),
        ('Dates', {'fields': ['created_at']}),
    ]
    

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['title', 'description', 'video', 'thumbnail', 'is_active']}),
        ('Dates', {'fields': ['created_at']}),
    ]
