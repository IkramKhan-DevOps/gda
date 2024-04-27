from django.urls import path
from .views import EventView, EventDetailView


app_name = 'events'
urlpatterns = [
path('events/', EventView.as_view(), name='events' ),
path('events/<slug:slug>/detail', EventDetailView.as_view(), name='event_detail' )
]
