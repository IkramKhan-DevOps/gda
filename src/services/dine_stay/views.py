from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .filters import DinningFilter, AccommodationFilter

from .models import Accommodation, AccommodationCategory, AccommodationFeature, AccommodationImages, Dining, \
    DiningAndAccommodationArea, DiningFeature, DiningImages
from ..events.models import Event

from .models import Accommodation, Dining
from src.services.events.models import Event, EventType



class AccommodationListView(ListView):
    model = Accommodation
    template_name = 'dine_stay/accommodations.html'

    paginate_by = 10



    def get_queryset(self):
        return Accommodation.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super(AccommodationListView, self).get_context_data(**kwargs)
        _filter = AccommodationFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_form'] = _filter.form
        paginator = Paginator(_filter.qs, 5)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context['object_list'] = page_object
        return context


class AccommodationDetailView(DetailView):
    model = Accommodation
    template_name = 'dine_stay/accommodation_details.html'
    context_object_name = 'accommodation'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accommodation = self.get_object()
        context['accommodation'] = accommodation
        context['accommodations'] = Accommodation.objects.filter(is_active=True)

        return context


class DiningListView(ListView):
    model = Dining
    template_name = 'dine_stay/dining.html'
    paginate_by = 10

    def get_queryset(self):
        dinings = Dining.objects.filter(is_active=True)
        return dinings

    def get_context_data(self, **kwargs):
        context = super(AccommodationDetailView, self).get_context_data(**kwargs)
        context['more_accommodation'] = Accommodation.objects.all()[:3]
        return context



class DiningDetailView(DetailView):
    model = Dining
    template_name = 'dine_stay/dining_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dining = self.get_object()
        context['dining'] = dining
        context['dinings'] = Dining.objects.filter(is_active=True)

        return context


class DiningListView(ListView):
    model = Dining
    template_name = 'dine_stay/dining.html'

    def get_context_data(self, **kwargs):
        context = super(DiningListView, self).get_context_data(**kwargs)
        _filter = DinningFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_form'] = _filter.form
        paginator = Paginator(_filter.qs, 5)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context['object_list'] = page_object
        return context


