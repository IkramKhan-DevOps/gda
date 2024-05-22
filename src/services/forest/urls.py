from django.urls import path
from .views import (
    WildlifeListView, WildlifeDetailView, WildlifeTypeListView,
    GreeneryListView, GreeneryDetailView, GreeneryTypeListView
)

app_name = 'forest'

urlpatterns = [
    # Wildlife URL patterns
    path('wildlife/<slug:slug>/', WildlifeListView.as_view(), name='wildlife_list'),
    path('wildlife/detail/<slug:slug>/', WildlifeDetailView.as_view(), name='wildlife_detail'),
    path('wildlife/types/', WildlifeTypeListView.as_view(), name='wildlife_type'),
    
    # Greenery URL patterns
    path('greenery/<slug:slug>/', GreeneryListView.as_view(), name='greenery_list'),
    path('greenery/detail/<slug:slug>/', GreeneryDetailView.as_view(), name='greenery_detail'),
    path('greenery/types/', GreeneryTypeListView.as_view(), name='greenery_type_list'),
]
