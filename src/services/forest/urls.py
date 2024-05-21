from django.urls import path
from .views import *

app_name = 'forest'
urlpatterns = [
path('wildlife/list', WildlifeListView.as_view(), name='wildlife_list'),
path('wildlife/<slug:slug>/', WildlifeDetailView.as_view(), name='wildlife_detail'),
path('wildlife/types/', WildlifeTypeListView.as_view(), name='wildlife_type'),

path('greenery/types/', GreeneryListView.as_view(), name='greenery_type' ),
path('greenery/<slug:slug>/', GreeneryDetailView.as_view(), name='greenery_detail'),
path('greenery/list/', GreeneryTypeListView.as_view(), name='greenery_list' ),
]
