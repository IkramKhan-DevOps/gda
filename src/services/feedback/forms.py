from django import forms

from src.services.feedback.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

        labels = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }

        placeholders = {
            'name': 'Enter Your Name*',
            'email': 'Enter Your Email*',
            'subject': 'Select Subject*',
            'message': 'Write Message',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': placeholders['name'],
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': placeholders['email'],
            }),
            'subject': forms.Select(choices=Contact.SUBJECT_CHOICE, attrs={
                'class': 'form-control',
                'placeholder': placeholders['subject'],
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': placeholders['message'],
            }),
        }
