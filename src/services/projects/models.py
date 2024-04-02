from django.db import models
from django_resized import ResizedImageField
from django_ckeditor_5.fields import CKEditor5Field

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    
    image = ResizedImageField(
        size=[500, 500], quality=75, upload_to='projects/images', blank=True, null=True,
        help_text='size of image must be 500*500 and format must be png image file'
    )
    video = models.URLField(max_length=100, blank=True, null=True, help_text='Add URL of video')
    
    is_active = models.BooleanField(default=True)
    is_ongoing = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(Projects, self).delete(*args, **kwargs)

    