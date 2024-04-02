from django.db import models
from django_resized import ResizedImageField


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = ResizedImageField(
        size=[500, 500], quality=100, upload_to='gallery/images', blank=True, null=True,
        help_text='size of logo must be 500*500 and format must be png image file'
    )
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        
    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(Image, self).delete(*args, **kwargs)
        
        
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    video = models.URLField(
        max_length=100,help_text='Enter the URL of the video' 
        )
    thumbnail = ResizedImageField(
        size=[500, 500], quality=75, upload_to='gallery/thumbnails', blank=True, null=True,
        help_text='size of logo must be 500*500 and format must be png image file'
    )
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        
    def delete(self, *args, **kwargs):
        self.video.delete(save=True)
        self.thumbnail.delete(save=True)
        super(Video, self).delete(*args, **kwargs)
        