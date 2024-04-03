from django.urls import path
from .views import *

app_name = 'departments'
urlpatterns = [
path('departments/', DepartmentListView.as_view(), name='departments'),

]
