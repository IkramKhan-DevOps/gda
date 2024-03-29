from django.contrib import admin

from .models import (
    Event, EventType,
)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'event_type', 'start_date', 'end_date', 'is_active', 'created_on']
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

