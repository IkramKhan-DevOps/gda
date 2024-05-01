from django.urls import path
from .views import EventListView, EventDetailView

app_name = 'events'
urlpatterns = [
    path('event/list/', EventListView.as_view(), name='event_list'),
    path('events/<str:slug>/detail', EventDetailView.as_view(), name='event_detail')
]
