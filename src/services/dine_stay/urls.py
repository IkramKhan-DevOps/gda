from django.urls import path
from .views import AccommodationListView, AccommodationDetailView, DiningListView, DiningDetailView

app_name = 'events'
urlpatterns = [
path('accommodations/', AccommodationListView.as_view(), name='accommodations'),
path('accommodations/<slug:slug>/', AccommodationDetailView.as_view(), name='hotel_details'),
path('dinings/', DiningListView.as_view(), name='dinings'),
path('dinings/<slug:slug>/', DiningDetailView.as_view(), name='dining_detail'),

]
