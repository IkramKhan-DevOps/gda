from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(blank=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        
    def __str__(self):
        return self.name
    