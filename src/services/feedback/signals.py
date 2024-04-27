from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Feedback


@receiver(post_save, sender=Feedback)
def send_feedback_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Feedback Submission'
        message = f'Name: {instance.name}\nEmail: {instance.email}\nSubject: {instance.subject}\nMessage: {instance.message}'
        sender_email = 'alikazmi855@email.com'  # --------> my email address
        recipient_list = ['alikazmi7767@email.com']  # ---------> receiver email address
        send_mail(subject, message, sender_email, recipient_list)
