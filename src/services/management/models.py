from django.db import models


class Download(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='downloads/files', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Download'
        verbose_name_plural = 'Downloads'

    def __str__(self):
        return self.title


class Archive(models.Model):
    name = models.ForeignKey(Download, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Archive'
        verbose_name_plural = 'Archives'


class Type(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Download, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self):
        return self.name
