from django.db import models
from django_resized import ResizedImageField
from django_ckeditor_5.fields import CKEditor5Field
from phonenumber_field.modelfields import PhoneNumberField


"""" ACCOMMODATIONS """


class AccommodationFeature(models.Model):
    name = models.CharField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Accommodation Feature'
        verbose_name_plural = 'Accommodation Features'
        
    def __str__(self):
        return self.name


class AccommodationCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Accommodation Category'
        verbose_name_plural = 'Accommodation Categories'

    def __str__(self):
        return self.name


class Accommodation(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    content = CKEditor5Field('Text', config_name='extends', null=True, blank=True)

    video = models.URLField(
        blank=True, null=True, help_text='Youtube video url'
    )
    thumbnail = ResizedImageField(
        size=[500, 500], quality=75, upload_to='dine_stay/accommodation/thumbnail', blank=True, null=True,
        help_text='size of thumbnail must be 500*500 and format must be png image file'
    )

    area = models.ManyToManyField('DiningAndAccommodationArea', related_name='accommodation_area', blank=True)
    category = models.ForeignKey(AccommodationCategory, on_delete=models.SET_NULL, blank=True, null=True)
    features = models.ManyToManyField(AccommodationFeature, related_name='features', blank=True)

    phone = PhoneNumberField(null=True, blank=False)
    email = models.EmailField(null=True, blank=True)

    website = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    address = models.CharField(max_length=1000)
    latitude = models.FloatField()
    longitude = models.FloatField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Accommodation'
        verbose_name_plural = 'Accommodations'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-').lower()
        super(Accommodation, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.thumbnail.delete(save=True)
        super(Accommodation, self).delete(*args, **kwargs)
        
        
class AccommodationImages(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.SET_NULL, related_name='accommodation_images', null = True)
    image = ResizedImageField(
        size=[500, 500], quality=75, upload_to='dine-stay/accommodation/images', blank=True, null=True,
        help_text='size of image must be 500*500 and format must be png image file'
    )

    class Meta:
        verbose_name = 'Accommodation Image'
        verbose_name_plural = 'Accommodation Images'

    def __str__(self):
        return self.accommodation.name


""" DINING """


class DiningFeature(models.Model):
    name = models.CharField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Dining Feature'
        verbose_name_plural = 'Dining Features'
        
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        super(DiningFeature, self).delete(*args, **kwargs)
        

class Dining(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    content = CKEditor5Field('Text', config_name='extends', null=True, blank=True)

    area = models.ManyToManyField('DiningAndAccommodationArea', related_name='dining_area', blank=True)
    features = models.ManyToManyField(DiningFeature, related_name='features', blank=True)
    
    video = models.URLField(
        blank=True, null=True, help_text='Youtube video url'
    )
    thumbnail = ResizedImageField(
        size=[500, 500], quality=75, upload_to='dine-stay/diningVenue/images', blank=True, null=True,
        help_text='size of thumbnail must be 500*500 and format must be png image file'
    )
    
    phone = PhoneNumberField(null=True, blank=False)
    email = models.EmailField(null=True, blank=True)

    website = models.URLField(null=True, blank=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    
    address = models.CharField(max_length=1000, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Dining'
        verbose_name_plural = 'Dining'

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.thumbnail.delete(save=True)
        super(Dining, self).delete(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-').lower()
        super(Dining, self).save(*args, **kwargs)
        

class DiningImages(models.Model):
    dining = models.ForeignKey(Dining, on_delete=models.SET_NULL, related_name='dining_images', null= True)
    image = ResizedImageField(
        size=[500, 500], quality=75, upload_to='dine-stay/diningVenue/images', blank=True, null=True,
        help_text='size of image must be 500*500 and format must be png image file'
    )

    class Meta:
        verbose_name = 'Dining Image'
        verbose_name_plural = 'Dining Images'

    def __str__(self):
        return self.dining.name
    
    
""" DINING and ACCOMMODATION Area"""

class DiningAndAccommodationArea(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='Name of the area e.g Nathiagali, Ayubia etc', null = True)
    image = ResizedImageField(
        size=[800, 600], quality=75, upload_to='dine-stay/area', help_text='size of image must be 800*600'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Area Dining and Accommodation'
        verbose_name_plural = 'Area Dining and Accommodations'
        
    def delete(self, *args, **kwargs):
        self.image.delete()
        super(DiningAndAccommodationArea, self).delete(*args, **kwargs)
        