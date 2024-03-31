from django.contrib import admin

from .models import (
    Event, EventType, EventImage, EventParticipant, Guest
)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'event_type', 'start_date', 'end_date', 'is_active', 'created_on', 'location',
                    'latitude', 'longitude']
    list_filter = ['event_type', 'is_active', 'created_on']
    search_fields = ['name']
    date_hierarchy = 'created_on'
    readonly_fields = ['created_on']
    fieldsets = [
        ('Event Information', {'fields': ['name', 'event_type', 'description', 'content', 'location']}),
        ('Event Dates', {'fields': ['start_date', 'end_date']}),
        ('Event Status', {'fields': ['is_active', 'created_on']}),
    ]


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_on']
    search_fields = ['name']


@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ['event', 'image', 'is_active', 'created_on']
    list_filter = ['is_active', 'created_on']
    search_fields = ['event']


@admin.register(EventParticipant)
class EventParticipantAdmin(admin.ModelAdmin):
    list_display = ['event', 'user', 'is_active', 'created_on']
    list_filter = ['is_active', 'created_on']
    search_fields = ['event', 'user']


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = [  'email', 'phone_number', 'is_active', 'created_on']
    list_filter = ['is_active', 'created_on']
    search_fields = ['event', 'name', 'email', 'phone_number']
