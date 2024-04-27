from django.contrib import admin
from .models import Feedback

admin.site.register(Feedback)
class Feedback(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at') 