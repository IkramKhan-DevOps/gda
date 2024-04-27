
from django.urls import path
from .views import AttractionAreaView, AttractionListView, AttractionDetailView

app_name = 'events'
urlpatterns = [
    path('attractions/area/', AttractionAreaView.as_view(), name='attractions_list'),
    path('attractions/<slug:slug>/points', AttractionListView.as_view(), name='attraction_points'),
    path('attractions/<slug:slug>/', AttractionDetailView.as_view(), name='attraction_detail'),
]
