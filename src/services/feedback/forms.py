from django import forms
from .models import Feedback

class CustomFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'feedback']
        label = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'feedback': 'Feedback',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        
