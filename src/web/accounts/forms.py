from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Div, Submit

from src.services.users.models import User
from src.web.service_provider.models import ServiceProvider


class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'profile_image', 'first_name', 'last_name',
            'phone_number'
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'profile_image']


class IncompleteServiceProviderForm(ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['name',
                  'logo', 'cover_image', 'description', 'contact_email',
                  'address', 'contact_phone',
                  'website', 'instagram', 'facebook', 'twitter'
                  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-sm-4'),
                Column('logo', css_class='form-group col-sm-6'),
                Column('cover_image', css_class='form-group col-sm-6'),
                Column('contact_email', css_class='col-sm-6'),
                Column('contact_phone', css_class='col-sm-6'),
                Column('address', css_class='col-sm-6 '),
                Column('website', css_class='col-sm-3'),
                Column('instagram', css_class='col-sm-3'),
                Column('facebook', css_class='col-sm-3'),
                Column('twitter', css_class='col-sm-3'),
                Column('description', css_class='col-sm-12'),
            ),
            Submit('submit', 'Submit', css_class='btn btn-success float-right')
        )


# class VehicleForm(ModelForm):
#     class Meta:
#         model = Vehicle
#         fields = ['registration_number', 'model', 'capacity', 'image', 'is_active']
