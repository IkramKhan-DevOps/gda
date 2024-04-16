from django.db import models
from django_resized import ResizedImageField
from django_ckeditor_5.fields import CKEditor5Field


class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=False, required = True,)
    email = models.EmailField(required=True, blank=False)
    subject = models.CharField(max_length=100, blank=False, required = True,)
    message = models.TextField(blank=False, required = True,)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        
    def __str__(self):
        return self.name
    