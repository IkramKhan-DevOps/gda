from django.db import models
from django_resized import ResizedImageField


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

    class Meta:
        ordering = ['-id']
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = ResizedImageField(
        size=[500, 500], quality=75, upload_to='management/department/images', blank=True, null=True,
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
    
