from django.views.generic import TemplateView

from .views import (
                    NewsLetterCreateView, ContactView, HomeTemplateView
                    )

from django.urls import path

app_name = "website"

# OFFICIAL
urlpatterns = [
    path('newsletter/create/', NewsLetterCreateView.as_view(), name='newsletter-create'),
    path('', HomeTemplateView.as_view(), name='home'),   
    
    path('act/', TemplateView.as_view(template_name='website/gda_act.html'), name='gda_act'),
    path('about/', TemplateView.as_view(template_name='website/about.html'), name='about'), 
    path('contact-us/', ContactView.as_view(), name='contact_us'),

    #                       --------Taxes---------
    path('watertax/',TemplateView.as_view(template_name='website/watertax.html'), name='watertax'),
    path('conservancytax/', TemplateView.as_view(template_name='website/conservancytax.html'), name='conservancytax'),
    path('propertytax/', TemplateView.as_view(template_name='website/property_tax.html'), name='propertytax'),
]