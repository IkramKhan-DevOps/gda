from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save

from src.services.feedback.models import Contact


@receiver(post_save, sender=Contact)
@receiver(post_save, sender=Contact)
def send_feedback_email(sender, instance, created, **kwargs):
    if created:
        department = instance.subject
        recipient_email = get_department_email(department)
        subject_user = 'Feedback Received'

        # Send Email to User
        message_user = 'Thank you for your feedback. We have received your message and will get back to you soon.'
        sender_email = 'cui1234567890987654321@gmail.com'
        recipient_list_user = [instance.email]

        # Send Email to Department
        subject_department = 'New Feedback Submission'
        message_department = f'Name: {instance.name}\nEmail: {instance.email}\nSubject: {instance.subject}\nMessage: {instance.message}'
        recipient_list_department = [recipient_email]

        send_mail(subject_user, message_user, sender_email, recipient_list_user)
        send_mail(subject_department, message_department, sender_email, recipient_list_department)


def get_department_email(department):
    department_emails = {
        'restaurants': 'zararanwar1234321@gmail.com',
        'tenders': 'tenders@example.com',
        'technical': 'technical@example.com',
    }
    return department_emails.get(department, 'default@example.com')
