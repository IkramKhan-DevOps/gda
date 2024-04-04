from django.db import models
from django_resized import ResizedImageField
from django_ckeditor_5.fields import CKEditor5Field


class Wildlife(models.Model):
    name = models.CharField(max_length=255)
    image = ResizedImageField(
        size=[800, 600], quality=75, upload_to='forest/wildlife', help_text='size of image must be 800*600'
        )
    content = CKEditor5Field(
        'Text', config_name='extends', null=True, blank=True, help_text='Description of the wildlife'
        )
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    
    is_active = models.BooleanField(
        default=True, help_text='Check to make it display on the website'
        )
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Wildlife'
        verbose_name_plural = 'Wildlife'

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-').lower()
        super(Wildlife , self).save(*args, **kwargs)

    
class Greenery(models.Model):
    name = models.CharField(
        max_length=255, help_text='Name of the plant,tree or flower etc'
        )
    image = ResizedImageField(
        size=[800, 600], quality=75, upload_to='forest/greenery', help_text='size of image must be 800*600'
        )
    content = CKEditor5Field(
        'Text', config_name='extends', null=True, blank=True, help_text='Description of the plant,tree or flower etc'
        )
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    
    types = models.ManyToManyField('GreeneryType', related_name='greenery', blank=True, help_text='Select the type of greenery')
    
    is_active = models.BooleanField(default=True, help_text='Check to make it display on the website')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Greenery'
        verbose_name_plural = 'Greenery'

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-').lower()
        super(Greenery, self).save(*args, **kwargs)


class GreeneryType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Greenery Type'
        verbose_name_plural = 'Greenery Types'
        
    def __str__(self):
        return self.name
