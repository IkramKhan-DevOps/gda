from .models import Event, EventType
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .filters import EventFilter


class EventListView(ListView):
    model = Event
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        _filter = EventFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_form'] = _filter.form
        paginator = Paginator(_filter.qs, 10)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context['object_list'] = page_object
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/eventdetail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['event_type'] = EventType.objects.all()[:5]
        context['latest_events'] = Event.objects.order_by("-created_at")[:5]
        return context
