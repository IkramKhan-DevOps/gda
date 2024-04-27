from .models import (
    Event
)
from django.views.generic import ListView, DetailView


class EventView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'
    paginate_by = 6

    def get_queryset(self):
        return Event.objects.filter(is_active=True).order_by('-id')

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/eventdetail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
