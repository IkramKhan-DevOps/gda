from django.contrib import admin

from .models import (
    AttractionFeature, Attraction, AttractionImage, AttractionCategory
)


@admin.register(AttractionFeature)
class AttractionFeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']
    list_per_page = 100


@admin.register(AttractionCategory)
class AttractionCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']
    list_per_page = 100


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {
            'fields': [
                'name', 'category', 'features', 'description',
            ],
        }),
        ('media', {'fields': ['thumbnail', 'video']}),
        ('location', {'fields': ['address', 'latitude', 'longitude']}),
        ('content', {'fields': ['content']}),
        ('Status and Dates', {'fields': ['is_active', 'created_at']}),

    ]
    list_display = ['id', 'name', 'address', 'latitude', 'longitude', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name', 'address']
    list_per_page = 100
    readonly_fields = ['created_at']


@admin.register(AttractionImage)
class AttractionImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'attraction', 'image', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['attraction__name']
    list_per_page = 100
