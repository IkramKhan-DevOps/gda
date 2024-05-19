from django.core.exceptions import ValidationError
from django.db import models
from django_resized import ResizedImageField

from phonenumber_field.modelfields import PhoneNumberField


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=2, unique=True, help_text='ISO 3166-1 alpha-2')
    language = models.CharField(max_length=3, default='en', help_text='ISO 639-1', null=True, blank=True)
    currency = models.CharField(max_length=3, default='USD', help_text='ISO 4217', null=True, blank=True)
    phone_code = models.CharField(max_length=4, default='+1', help_text='e.g. +1', null=True, blank=True)

    is_services_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class NewsLetter(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'News Letters'

    def __str__(self):
        return self.email

    def clean(self):
        if NewsLetter.objects.filter(email=self.email).exists():
            raise ValidationError(f"{self.email} you have already subscribed to our newsletter.")


class Application(models.Model):
    name = models.CharField(max_length=100, help_text='Application name', default='Exarth')
    short_name = models.CharField(max_length=10, help_text='Your application short name', default='EX')
    tagline = models.CharField(
        max_length=100, help_text='Your application business line', default='Your digital partner'
    )
    description = models.TextField(
        default="Add your project description here.", help_text='Application Description'
    )

    favicon = ResizedImageField(
        upload_to='core/application/images',
        null=True, blank=True, size=[250, 250], quality=75, force_format='PNG',
        help_text='Application favicon'
    )
    logo = ResizedImageField(
        upload_to='core/application/images', null=True, blank=True, size=[500, 500], quality=75, force_format='PNG',
        help_text='Application real colors logo'
    )
    logo_dark = ResizedImageField(
        upload_to='core/application/images', null=True, blank=True, size=[500, 500], quality=75, force_format='PNG',
        help_text='For dark theme only'
    )
    logo_light = ResizedImageField(
        upload_to='core/application/images', null=True, blank=True, size=[500, 500], quality=75, force_format='PNG',
        help_text='For light theme only'
    )

    contact_email1 = models.EmailField(
        max_length=100, default='support@exarth.com', help_text='Application contact email 1'
    )
    contact_email2 = models.EmailField(
        max_length=100, default='support@exarth.com', help_text='Application contact email 2'
    )
    contact_phone1 = PhoneNumberField(
        help_text='Application contact phone 1', default='+923419387283'
    )
    contact_phone2 = PhoneNumberField(
        help_text='Application contact phone 2', default='+923259575875'
    )

    address = models.CharField(
        max_length=255, help_text='office address', default='your main office address'
    )
    latitude = models.DecimalField(max_digits=10, decimal_places=6, help_text='latitude', default=23.7)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, help_text='longitude', default=90.3)

    terms_url = models.URLField(
        max_length=255, default='https://exarth.com/terms-of-use/', help_text='Terms and Conditions page link'
    )

    facebook = models.URLField(
        max_length=255, default='https://exarth.com/terms-of-use/', help_text='Social Facebook link'
    )
    instagram = models.URLField(
        max_length=255, default='https://exarth.com/terms-of-use/', help_text='Social Instagram link'
    )
    twitter = models.URLField(
        max_length=255, default='https://exarth.com/terms-of-use/', help_text='Social Twitter link'
    )

    version = models.CharField(max_length=10, help_text='Current version', default='1.0.0')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Application"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self,  *args, **kwargs):
        if Application.objects.exists() and not self.pk:
            raise ValidationError("Only one record allowed.")
        super(Application, self).save(*args, **kwargs)


