from django.contrib import admin

from .models import (
    Event, EventType, EventImage, Participant, Guest
)


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 3


class GuestInline(admin.TabularInline):
    model = Guest
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'event_type', 'location', 'latitude', 'longitude', 'start_date', 'end_date', 'is_active'
    ]
    list_filter = ['event_type', 'is_active']
    search_fields = ['name']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['name', 'event_type', 'description']}),
        ('Images', {'fields': ['thumbnail', 'banner']}),
        ('Content', {'fields': ['content']}),
        ('Location', {'fields': ['latitude', 'longitude', 'location']}),
        ('Status', {'fields': ['is_active']}),
        ('Dates', {'fields': ['start_date', 'end_date', 'created_at']}),
    ]
    inlines = [EventImageInline, GuestInline]


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at']
    search_fields = ['name']


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'user', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['event', 'user']
