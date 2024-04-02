from django.db import models
from django_resized import ResizedImageField
from django_ckeditor_5.fields import CKEditor5Field
from phonenumber_field.modelfields import PhoneNumberField

class TagAccommodation(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tag Accommodation'
        verbose_name_plural = 'Tag Accommodations'
        
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        super(TagAccommodation, self).delete(*args, **kwargs)
        
        
        
class TagDiningVenue(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tag Dining Venue'
        verbose_name_plural = 'Tag Dining Venues'
        
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        super(TagAccommodation, self).delete(*args, **kwargs)



class Type(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    image = ResizedImageField( 
        size=[500, 500], quality=100, upload_to='dine-stay/type/images', blank=True, null=True,
        help_text='size of logo must be 500*500 and format must be png image file'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(Type, self).delete(*args, **kwargs)
        
        


class Accommodation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    content = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    features = models.ManyToManyField(TagAccommodation, related_name='attractions')
    
    image = ResizedImageField(
        size=[800, 800], quality=100, upload_to='dine-stay/accommodation/images', blank=True, null=True,
        help_text='size of image must be 800*800 and format must be png image file'
    )
    video = models.URLField(
        max_length=100, blank=True, null=True, help_text='Add URL of video')
    thumbnail = ResizedImageField(
        size=[500, 500], quality=75, upload_to='dine-stay/accommodation/images', blank=True, null=True,
        help_text='size of thumbnail must be 500*500 and format must be png image file'
    )
    
    
    is_active = models.BooleanField(default=True)
    stay_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    
    phone =PhoneNumberField(blank=True, null=True, )
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=100)
    
    address = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Accommodation'
        verbose_name_plural = 'Accommodations'

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(Accommodation, self).delete(*args, **kwargs)
        
        


class DiningVenue(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    content = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    features = models.ManyToManyField(TagDiningVenue, related_name='DiningVenues')
    
    image = ResizedImageField(
        size=[800, 800], quality=100, upload_to='dine-stay/diningVenue/images', blank=True, null=True,
        help_text='size of image must be 800*800 and format must be png image file'
    )
    video = models.URLField(
        max_length=100, blank=True, null=True, help_text='Add URL of video')
    thumbnail = ResizedImageField(
        size=[500, 500], quality=75, upload_to='dine-stay/diningVenue/images', blank=True, null=True,
        help_text='size of thumbnail must be 500*500 and format must be png image file'
    )
    
    is_active = models.BooleanField(default=True)
    
    phone = PhoneNumberField(blank=True, null=True, )
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=100)
    
    address = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Dining Venue'
        verbose_name_plural = 'Dining Venues'

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(DiningVenue, self).delete(*args, **kwargs)
        