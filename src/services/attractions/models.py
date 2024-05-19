from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField


class AttractionFeature(models.Model):
    name = models.CharField(max_length=100, unique=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.name


class AttractionCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Attraction(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    area = models.ForeignKey('AttractionArea', related_name='attractions', on_delete=models.SET_NULL, null=True,
                             blank=False)
    category = models.ForeignKey(
        AttractionCategory, related_name='attractions', on_delete=models.SET_NULL, null=True, blank=False
    )

    description = models.TextField(help_text='Short description of attraction point')
    content = CKEditor5Field('Text', config_name='extends', null=True, blank=True)

    features = models.ManyToManyField(AttractionFeature, related_name='attractions', blank=True)
    thumbnail = ResizedImageField(
        size=[500, 500], quality=75, upload_to='attractions/attraction/thumbnail', blank=False, null=True,
        help_text='Size of image must be 500*500 and format must be png image file'
    )
    video = models.URLField(
        max_length=100, blank=True, null=True, help_text='Youtube video link'
    )

    address = models.CharField(max_length=100, help_text='Address of attraction point i.e Lahore, Pakistan')
    latitude = models.FloatField(help_text='Latitude of attraction point i.e 31.5204', blank=True, null=True)
    longitude = models.FloatField(help_text='Longitude of attraction point i.e 74.3587', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Point'
        verbose_name_plural = 'Points'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Attraction, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.thumbnail.delete(save=True)
        super(Attraction, self).delete(*args, **kwargs)


class AttractionImage(models.Model):
    attraction = models.ForeignKey(Attraction, related_name='images', on_delete=models.CASCADE)
    image = ResizedImageField(
        size=[500, 500], quality=75, upload_to='attractions/attraction/images', blank=True, null=True,
        help_text='Size of image must be 500*500 and format must be png image file'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.attraction.name


class AttractionArea(models.Model):
    name = models.CharField(max_length=100, unique=True)
    detail = models.TextField(help_text='Short description of area', null=True, blank=False)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    image = ResizedImageField(
        size=[800, 600], quality=75, upload_to='attractions/attraction/area', help_text='Size of image must be 800*600',
        null=True
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(AttractionArea, self).save(*args, **kwargs)
