from django.db import models
from django_resized import ResizedImageField
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify

class Wildlife(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, help_text='short description of the wildlife', null = True)
    content = CKEditor5Field(
        'Text', config_name='extends', null=True, blank=True, help_text='Description of the wildlife'
        )
    
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    types = models.ManyToManyField('WildlifeType', related_name='type', blank=True, help_text='Select the type of wildlife eg birds, animals etc')
    image = ResizedImageField(
        size=[800, 600], quality=75, upload_to='forest/wildlife', help_text='size of image must be 800*600'
        )
    
    scientific_name = models.CharField(max_length=255, help_text='Scientific name of the wildlife', null=True)
    is_active = models.BooleanField(default=True, help_text='Check to make it display on the website')
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
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class WildlifeType(models.Model):
    name = models.CharField(max_length=255, help_text='Name of the wildlife type eg birds, animals etc')
    image = ResizedImageField(
        size=[800, 600], quality=75, upload_to='forest/wildlife/type', help_text='size of image must be 800*600', null=True
        )
    
    details = models.CharField(max_length=255,default="GDA is working on ways to save these type of species more", help_text="Write details about the type")
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Wildlife type'
        verbose_name_plural = 'Wildlife types'
        
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
        
    
class Greenery(models.Model):
    name = models.CharField(
        max_length=255, help_text='Name of the plant,tree or flower etc'
        )
    scientific_name = models.CharField( max_length=255, help_text='Scientific name of the plant,tree or flower etc', null=True)
    image = ResizedImageField(
        size=[800, 600], quality=75, upload_to='forest/greenery', help_text='size of image must be 800*600'
        )
    description = models.TextField(max_length=255, help_text='short description of the greenery', null = True)
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
    name = models.CharField(max_length=255, help_text='Name of the greenery type eg plants, trees etc')
    image = ResizedImageField(
        size=[800, 600], quality=75, upload_to='forest/greenery/type', help_text='size of image must be 800*600', null=True
        )
    
    details = models.CharField(max_length=255, help_text="Write details about the type",default="GDA is working on Preserving its Forests to Keep Galiyat Green")
    

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Greenery Type'
        verbose_name_plural = 'Greenery Types'
        
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)