from django.contrib import admin

from src.services.feedback.models import Contact

admin.site.register(Contact)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at')

