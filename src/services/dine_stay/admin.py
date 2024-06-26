from django.contrib import admin
from .models import (
    Accommodation, AccommodationCategory, Dining, AccommodationFeature, DiningFeature, AccommodationImages, DiningImages, DiningAndAccommodationArea
)


"""" ACCOMMODATIONS """


@admin.register(AccommodationFeature)
class AccommodationFeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']


@admin.register(AccommodationCategory)
class AccommodationCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']


class AccommodationImageInline(admin.TabularInline):
    model = AccommodationImages
    extra = 3


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'phone', 'email', 'is_active', 'created_at']
    list_filter = ['is_active', 'category', 'features']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['name', 'category', 'features']}),
        ('media', {'fields': ['video', 'thumbnail']}),
        ('Contact', {'fields': ['phone', 'email']}),
        ('Social Links', {'fields': ['website', 'facebook', 'instagram']}),
        ('Location', {'fields': ['area','address', 'latitude', 'longitude']}),
        ('content', {'fields': ['description', 'content']}),
        ('Status and Dates', {'fields': ['is_active', 'created_at']}),
    ]
    inlines = [AccommodationImageInline]

""" DINING """

@admin.register(DiningFeature)
class DiningFeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']

class DiningImageInline(admin.TabularInline):
    model = DiningImages
    extra = 3


@admin.register(Dining)
class DineAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'is_active', 'created_at']
    list_filter = ['is_active', 'features']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['name', 'features']}),
        ('media', {'fields': ['video', 'thumbnail']}),
        ('Contact', {'fields': ['phone', 'email']}),
        ('Social Links', {'fields': ['website', 'facebook', 'instagram']}),
        ('Location', {'fields': ['area','address', 'latitude', 'longitude']}),
        ('content', {'fields': ['description', 'content']}),
        ('Status and Dates', {'fields': ['is_active', 'created_at']}),
    ]

    inlines = [DiningImageInline]
    
    
""" DINING AND ACCOMMODATION AREA """
@admin.register(DiningAndAccommodationArea)
class DiningAndAccommodationAreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    fieldsets = [
        ('', {'fields': ['name']}),
    ]