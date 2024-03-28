from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from src.services.users.models import User


class ServiceProvider(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='agency_logos/', null=True, blank=True)
    cover_image = models.ImageField(upload_to='agency_covers/', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    contact_email = models.EmailField()

    is_completed = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    website = models.URLField(max_length=255, null=True, blank=True)
    instagram = models.URLField(max_length=255, null=True, blank=True)
    facebook = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Service_Provider'
        ordering = ['name']

    def __str__(self):
        return self.name

