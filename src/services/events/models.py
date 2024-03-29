from django.db import models
from django_resized import ResizedImageField


class EventType(models.Model):
    name = models.CharField(max_length=100)
    image = ResizedImageField(
        size=[500, 500], quality=100, upload_to='events/images/event-type', blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Event Type'
        verbose_name_plural = 'Event Types'

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)

    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    location = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name

