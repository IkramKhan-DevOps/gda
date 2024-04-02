from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField


class TagAttraction(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tag Accommodation'
        verbose_name_plural = 'Tag Accommodations'
        
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        super(TagAttraction, self).delete(*args, **kwargs)
        
        

class AttractionPoint(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    content = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    features = models.ManyToManyField(TagAttraction, related_name='attractions')
    
    image = ResizedImageField(
        size=[500, 500], quality=75, upload_to='attractions/tourism/images', blank=True, null=True,
        help_text='size of image must be 500*500 and format must be png image file'
    )
    video = models.URLField(
        max_length=100, blank=True, null=True, help_text='Add URL of video'
        )
    thumbnail = ResizedImageField(
        size=[500, 500], quality=75, upload_to='attractions/tourism/images', blank=True, null=True,
        help_text='size of thumbnail must be 500*500 and format must be png image file'
    )
    
    
    is_active = models.BooleanField(default=True)


    address = models.CharField(max_length=100)
    area = models.CharField(max_length=100, blank=True, null=True)
    lat = models.FloatField()
    lon = models.FloatField()
    
        
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Attraction Point'
        verbose_name_plural = 'Attraction Points'
    
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.thumbnail.delete(save=True)
        super(AttractionPoint, self).delete(*args, **kwargs)

    