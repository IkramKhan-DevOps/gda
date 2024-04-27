from django.contrib import admin
from .models import Visit

admin.site.register(Visit)
class Counter(admin.ModelAdmin):
    list_display = ('count')