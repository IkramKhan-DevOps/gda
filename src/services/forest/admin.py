from django.contrib import admin
from .models import Greenery, GreeneryType, Wildlife, WildlifeType

@admin.register(Greenery)
class GreeneryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'id')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('', {'fields': ('name', 'image', 'content','description','is_active', 'types')}),
        ('Dates', {'fields': ('created_at',)}),
    )
    
@admin.register(GreeneryType)
class GreeneryTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fieldsets = (
        ('', {'fields': ('name','details', 'image')}),
    )
    
@admin.register(Wildlife)
class WildlifeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'id')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('', {'fields': ('name','scientific_name', 'image','description', 'content', 'is_active', 'types' )}),
        ('Dates', {'fields': ('created_at',)}),
        
    )

@admin.register(WildlifeType)
class WildlifeTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fieldsets = (
        ('', {'fields': ('name','details', 'image')}),
    )
    