from django.contrib import admin
from .models import Projects, Department, Directors, DirectorGeneral

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['title', 'description', 'is_active']}),
        ('content', {'fields': ['content', 'image', 'video']}),
        ('Dates', {'fields': ['created_at']}),
    ]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name']
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['name', 'description', 'rank', 'image', 'message', 'is_active']}),
        ('Dates', {'fields': ['created_at']}),
    ]


@admin.register(Directors)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department', 'created_at']
    list_filter = ['department', 'created_at']
    search_fields = ['name']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['image','name', 'message', 'department']}),
        ('Dates', {'fields': ['created_at']}),
    ]
    
    
@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    fieldsets = [
        ('', {'fields': ['image','name', 'message']}),
        ('Dates', {'fields': ['created_at']}),
    ]