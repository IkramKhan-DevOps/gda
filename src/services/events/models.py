from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField


class EventType(models.Model):
    name = models.CharField(max_length=100)
    image = ResizedImageField(
        size=[500, 500], quality=100, upload_to='events/event-type/images', blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Event Type'
        verbose_name_plural = 'Event Types'

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(EventType, self).delete(*args, **kwargs)


class Event(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)

    thumbnail = ResizedImageField(
        size=[500, 500], quality=75, upload_to='events/event/images', blank=True, null=True,
        help_text='size of logo must be 500*500 and format must be png image file'
    )
    banner = ResizedImageField(
        quality=75, upload_to='events/event/images', blank=True, null=True,
        help_text='size of logo must be banner size and format must be png image file'
    )

    description = models.TextField(blank=True, null=True)
    content = CKEditor5Field('Text', config_name='extends', null=True, blank=True)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    location = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-').lower()
        super(Event, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.thumbnail.delete(save=True)
        self.banner.delete(save=True)
        super(Event, self).delete(*args, **kwargs)


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = ResizedImageField(
        size=[800, 800], quality=100, upload_to='events/event/images', blank=True, null=True,
        help_text='size of logo must be 800*800 and format must be png image file'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Event Image'
        verbose_name_plural = 'Event Images'

    def __str__(self):
        return self.event.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(EventImage, self).delete(*args, **kwargs)


class Participant(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True, )
    address = models.TextField(blank=True, null=True)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'

    def __str__(self):
        return f'{self.user.email} - {self.event.name}'


class Guest(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True, )
    designation = models.CharField(max_length=100, blank=True, null=True)
    image = ResizedImageField(
        size=[500, 500], quality=100, upload_to='events/guest/images', blank=True, null=True,
        help_text='size of logo must be 500*500 and format must be png image file'
    )

    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'

    def __str__(self):
        return self.full_name

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(Guest, self).delete(*args, **kwargs)
