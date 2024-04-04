from django.contrib import admin
from .models import Greenery, GreeneryType, Wildlife

@admin.register(Greenery)
class GreeneryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'id')
    fieldsets = (
        ('', {'fields': ('name', 'image', 'content', 'types')}),
        ('Status', {'fields': ('is_active',)}),
    )
    
@admin.register(GreeneryType)
class GreeneryTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fieldsets = (
        ('', {'fields': ('name',)}),
    )
    
@admin.register(Wildlife)
class WildlifeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'id')
    fieldsets = (
        ('', {'fields': ('name', 'image', 'content')}),
        ('Status', {'fields': ('is_active',)}),
    )
