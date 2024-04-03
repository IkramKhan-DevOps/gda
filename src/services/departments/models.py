from django.db import models
from django_resized import ResizedImageField
from django_ckeditor_5.fields import CKEditor5Field


""" Department And Personnel Models """
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = ResizedImageField(
        size=[500, 500], quality=75, upload_to='projects/department/images', blank=True, null=True,
        help_text='size of image must be 500*500 and format must be png image file'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name
    
    
class Personnel(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    image = ResizedImageField(
        size=[500, 500], quality=75, upload_to='projects/ Personnel/images', blank=True, null=True,
        help_text='The size of the image must be 500*500 and the format must be a PNG image file.'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Directors(Personnel):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'
    
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(Directors, self).delete(*args, **kwargs)


class DirectorGeneral(Personnel):
    department = models.CharField(max_length=100, default="Director General")
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Director General'
        verbose_name_plural = 'Director Generals'
    
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(Directors, self).delete(*args, **kwargs)
        
        
""" Projects Models """
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
