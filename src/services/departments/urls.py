from django.urls import path
from .views import *

app_name = 'departments'
urlpatterns = [
path('departments/', DepartmentListView.as_view(), name='departments'),
path('department/<slug:slug>/detail', DepartmentDetailView.as_view(), name='department_detail'),
path('team/', PersonalsView.as_view(), name='gda_team'),

]
