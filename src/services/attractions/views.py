from django.core.paginator import Paginator

from .filters import AttractionAreaFilter, AttractionPointFilter
from .models import Attraction, AttractionArea
from django.views.generic import ListView, DetailView, TemplateView, View


class AttractionAreaView(ListView):
    model = AttractionArea
    template_name = 'attractions/attraction_areas.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return AttractionArea.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super(AttractionAreaView, self).get_context_data(**kwargs)
        _filter = AttractionAreaFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_form'] = _filter.form
        paginator = Paginator(_filter.qs, 20)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context['object_list'] = page_object
        return context


class AttractionListView(ListView):
    model = Attraction
    template_name = 'attractions/attraction_points_list.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return self.model.objects.filter(area__slug=self.kwargs['slug'], is_active=True)

    def get_context_data(self, **kwargs):
        context = super(AttractionListView, self).get_context_data(**kwargs)
        _filter = AttractionPointFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_form'] = _filter.form
        paginator = Paginator(_filter.qs, 20)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context['object_list'] = page_object
        context['area_name'] = AttractionArea.objects.filter(slug=self.kwargs.get('slug')).first()
        return context


class AttractionDetailView(DetailView):
    model = Attraction
    template_name = 'attractions/attraction_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

