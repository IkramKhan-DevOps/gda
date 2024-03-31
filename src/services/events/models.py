from django.db import models
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField


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
    name = models.CharField(max_length=100, unique=True)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)

    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    location = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-').lower()
        super(Event, self).save(*args, **kwargs)


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = ResizedImageField(
        size=[800, 800], quality=100, upload_to='events/images/event', blank=True, null=True
    )
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Event Image'
        verbose_name_plural = 'Event Images'

    def __str__(self):
        return self.event.name


class EventParticipant(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True, )
    address = models.TextField(blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Event Participant'
        verbose_name_plural = 'Event Participants'

    def __str__(self):
        return f'{self.user.email} - {self.event.name}'


class Guest(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True, )
    designation = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'

    def __str__(self):
        return self.full_name
