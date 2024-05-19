from django.db import models
from django_resized import ResizedImageField
from django_ckeditor_5.fields import CKEditor5Field

"""DOCUMENT MODELS"""


class DocumentType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Document Type'
        verbose_name_plural = 'Document Types'

    def __str__(self):
        return self.name


# TODO: Add document file validation and file is required [in deployment]
class Document(models.Model):
    title = models.CharField(max_length=100, unique=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, blank=False, null=True)
    description = models.TextField(blank=True, null=True, help_text="Document description.")

    file = models.FileField(
        upload_to='management/download/files', blank=True, null=True,
        help_text="Document file of type PDF, DOC, DOCX, etc."
    )

    is_active = models.BooleanField(default=True, help_text="Active documents are displayed on the website.")
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title


"""Gallery Models"""


class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = ResizedImageField(
        size=[500, 500], quality=100, upload_to='management/gallery/images', blank=True, null=True,
        help_text='size of logo must be 500*500 and format must be png image file'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(GalleryImage, self).delete(*args, **kwargs)


class GalleryVideo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    video = models.URLField(
        max_length=100, help_text='Enter the URL of the video'
    )
    thumbnail = ResizedImageField(
        size=[500, 500], quality=75, upload_to='management/gallery/thumbnails', blank=True, null=True,
        help_text='size of logo must be 500*500 and format must be png image file'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Gallery Video'
        verbose_name_plural = 'Gallery Videos'

    def delete(self, *args, **kwargs):
        self.thumbnail.delete(save=True)
        super(GalleryVideo, self).delete(*args, **kwargs)


"""News Models"""


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = CKEditor5Field('Text', config_name='extends', null=True, blank=True, help_text='Add content here')
    thumbnail = ResizedImageField(
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


class NewsImages(models.Model):
    news = models.ForeignKey(News, on_delete=models.SET_NULL, related_name='images', null=True)
    image = ResizedImageField(
        size=[500, 500], quality=75, upload_to='news/images', blank=True, null=True,
        help_text='size of image must be 500*500 and format must be png image file'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'News Image'
        verbose_name_plural = 'News Images'

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(NewsImages, self).delete(*args, **kwargs)


class HomeSlider(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=250)
    image = ResizedImageField(
        size=[500, 500], quality=75, upload_to='news/images', blank=True, null=True,
        help_text='size of image must be 500*500 and format must be png image file'
    )
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Home Slider Image'
        verbose_name_plural = 'Home Slider Images'


class WeatherLocation(models.Model):
    latitude = models.FloatField(default='34.07')
    longitude = models.FloatField(default='73.38')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Weather Location'
        verbose_name_plural = 'Weather Locations'

    def __str__(self):
        return f"Location"
