from django.contrib import admin
from .models import (
    Document, DocumentType, GalleryImage, GalleryVideo, News, NewsImages, HomeSlider
)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'file', 'document_type', 'is_active', 'created_at']


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name']


@admin.register(GalleryImage)
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


@admin.register(GalleryVideo)
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


class NewsImagesInline(admin.TabularInline):
    model = NewsImages
    extra = 3


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('', {'fields': ['title', 'description', 'is_active']}),
        ('content', {'fields': ['content', 'thumbnail']}),
        ('Dates', {'fields': ['created_at', 'updated_at']}),
    ]
    inlines = [NewsImagesInline]


@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'tagline']
