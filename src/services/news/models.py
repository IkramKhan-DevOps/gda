from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    image = ResizedImageField(
        size=[500, 500], quality=75, upload_to='news/images', blank=True, null=True,
        help_text='size of image must be 500*500 and format must be png image file'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(News, self).delete(*args, **kwargs)