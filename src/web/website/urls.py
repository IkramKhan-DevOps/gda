from .views import home, about
from django.urls import path
app_name = "website"
urlpatterns = [
     path('', home, name='home'),
     path('about/', about, name='about')
]
