from django.urls import path
from .views import *

urlpatterns = [
     path('feedback/', FormView.as_view(), name='feedback'),
]
