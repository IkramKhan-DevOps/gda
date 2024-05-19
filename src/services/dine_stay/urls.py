from django.urls import path
from .views import AccommodationListView, AccommodationDetailView, DiningListView, DiningDetailView

app_name = 'diny_stay'
urlpatterns = [
    path('accommodations/', AccommodationListView.as_view(), name='accommodations'),
    path('accommodation/detail/<str:pk>/', AccommodationDetailView.as_view(), name='accommodation-detail'),
    path('dinings/', DiningListView.as_view(), name='dinings'),
    path('dinings/<str:pk>/', DiningDetailView.as_view(), name='dining_detail'),

]
