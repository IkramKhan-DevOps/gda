from django.contrib import admin

from .models import (
    AttractionPoint, TagAttraction
)

@admin.register(AttractionPoint)
class AttractionPointAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['name', 'description','features', 'is_active']}),
        ('content', {'fields': ['content', 'image', 'video', 'thumbnail']}),
        ('Location', {'fields': ['address','area', 'lat', 'lon']}),
        ('Dates', {'fields': ['created_at']}),
    ]



@admin.register(TagAttraction)
class TagAttractionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']
    fieldsets = [
        ('', {'fields': ['name', 'is_active']}),
    ]
    
    def delete(self, *args, **kwargs):
        super(TagAttraction, self).delete(*args, **kwargs)