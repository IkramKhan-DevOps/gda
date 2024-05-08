from django.urls import path
from .views import EventListView, EventDetailView

app_name = 'events'
urlpatterns = [
    path('event/list/', EventListView.as_view(), name='event_list'),
    path('event/<str:slug>/detail', EventDetailView.as_view(), name='event_detail')
]
