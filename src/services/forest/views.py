from django.views.generic import ListView, DetailView
from .models import Greenery, Wildlife, WildlifeType, GreeneryType
from .filters import GreeneryFilter, GreeneryTypeFilter, WildLifeFilter, WildLifeTypeFilter
from django.core.paginator import Paginator


class WildlifeListView(ListView):
    model = Wildlife
    template_name = 'forest/wildlife.html'
    paginate_by = 6
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return self.model.objects.filter(area__slug=self.kwargs['slug'], is_active=True)

    def get_context_data(self, **kwargs):
        context = super(WildlifeListView, self).get_context_data(**kwargs)
        _filter = WildLifeFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_form'] = _filter.form
        paginator = Paginator(_filter.qs, 20)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context['object_list'] = page_object
        context['area_name'] = Wildlife.objects.filter(slug=self.kwargs.get('slug')).first()
        return context
    
    
class WildlifeDetailView(DetailView):
    model = Wildlife
    template_name = 'forest/wildlife_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(GreeneryDetailView, self).get_context_data(**kwargs)
        context['attraction_category'] = WildlifeType.objects.all()[:15]
        context['latest_attractions'] = Wildlife.objects.filter(area_id__in=WildlifeType.objects.all())
        return context


class WildlifeTypeListView(ListView):
    model = WildlifeType
    template_name = 'forest/wildlife_type.html'

    def get_queryset(self):
        return WildlifeType.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super(WildlifeTypeListView, self).get_context_data(**kwargs)
        _filter = WildLifeTypeFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_form'] = _filter.form
        paginator = Paginator(_filter.qs, 20)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context['object_list'] = page_object
        return context


class GreeneryListView(ListView):
    model = Greenery
    template_name = 'forest/greenery_list.html'
    context_object_name = 'greenery_list'
    paginate_by = 6
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return self.model.objects.filter(area__slug=self.kwargs['slug'], is_active=True)

    def get_context_data(self, **kwargs):
        context = super(GreeneryListView, self).get_context_data(**kwargs)
        _filter = GreeneryFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_form'] = _filter.form
        paginator = Paginator(_filter.qs, 20)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context['object_list'] = page_object
        context['area_name'] = Greenery.objects.filter(slug=self.kwargs.get('slug')).first()
        return context
    
    
class GreeneryDetailView(DetailView):
    model = Greenery
    template_name = 'forest/greenery_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(GreeneryDetailView, self).get_context_data(**kwargs)
        context['attraction_category'] = GreeneryType.objects.all()[:15]
        context['latest_attractions'] = Greenery.objects.filter(area_id__in=GreeneryType.objects.all())
        return context

    
    
class GreeneryTypeListView(ListView):
    model = GreeneryType
    template_name = 'forest/greenery_type.html'
    paginate_by = 6
    
    def get_queryset(self):
        return GreeneryType.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super(GreeneryTypeListView, self).get_context_data(**kwargs)
        _filter = GreeneryTypeFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_form'] = _filter.form
        paginator = Paginator(_filter.qs, 20)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context['object_list'] = page_object
        return context
