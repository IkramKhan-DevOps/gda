from django.contrib import admin

from .models import (
    Event, EventType, EventImage, Participant, Guest
)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'event_type', 'location', 'latitude', 'longitude', 'start_date', 'end_date', 'is_active'
    ]
    list_filter = ['event_type', 'is_active']
    search_fields = ['name']
    date_hierarchy = 'created_on'
    readonly_fields = ['created_on']
    fieldsets = [
        ('', {'fields': ['name', 'event_type', 'description']}),
        ('Images', {'fields': ['thumbnail', 'banner']}),
        ('Content', {'fields': ['content']}),
        ('Location', {'fields': ['latitude', 'longitude', 'location']}),
        ('Status', {'fields': ['is_active']}),
        ('Dates', {'fields': ['start_date', 'end_date', 'created_on']}),
    ]


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_on']
    search_fields = ['name']


@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'image', 'is_active', 'created_on']
    list_filter = ['is_active']
    search_fields = ['event']


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'user', 'is_active', 'created_on']
    list_filter = ['is_active', 'created_on']
    search_fields = ['event', 'user']


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone_number', 'designation', 'is_active', 'created_on']
    search_fields = ['event', 'full_name', 'email', 'phone_number']
    list_filter = ['is_active', 'event']
