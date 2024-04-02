from django.contrib import admin
from .models import (
    Accommodation, Type, DiningVenue, TagAccommodation, TagDiningVenue
    )


@admin.register(Accommodation)
class StayAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description',  'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('', {'fields': ['name', 'description','features', 'is_active', 'stay_type']}),
        ('Contact', {'fields': ['phone', 'email', 'website']}),
        ('Location', {'fields': ['address', 'lat', 'lon']}),
        ('Dates', {'fields': ['created_at', 'updated_at']}),
        ('content', {'fields': ['content','image', 'video', 'thumbnail']}),
    ]

    

@admin.register(DiningVenue)
class DineAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at', 'content', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('', {'fields': ['name', 'description','features', 'is_active']}),
        ('Contact', {'fields': ['phone', 'email', 'website']}),
        ('Location', {'fields': ['address', 'lat', 'lon']}),
        ('Dates', {'fields': ['created_at', 'updated_at']}),
        ('content', {'fields': ['content','image`', 'video', 'thumbnail']})
    ]
    


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('', {'fields': ['name', 'image', 'is_active']}),
        ('Dates', {'fields': ['created_at', 'updated_at']}),
    ]
    
    
@admin.register(TagAccommodation)
class TagAccommodationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']
    fieldsets = [
        ('', {'fields': ['name', 'is_active']}),
    ]
    
@admin.register(TagDiningVenue)
class TagDiningVenueAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']
    fieldsets = [
        ('', {'fields': ['name', 'is_active']}),
    ]
