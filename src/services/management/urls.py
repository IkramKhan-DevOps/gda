from django.urls import path

from src.services.management.views import DocumentListView

app_name = 'management'
urlpatterns = [
    path('dowmload/', DocumentListView.as_view(), name='document-list'),
]
