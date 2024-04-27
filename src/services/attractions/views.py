from .models import Attraction,AttractionArea
from django.views.generic import ListView, DetailView, TemplateView, View


class AttractionAreaView(ListView):
    model = AttractionArea
    template_name = 'attractions/attraction_areas.html'
    paginate_by = 10
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return AttractionArea.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['areas'] = self.get_queryset()
        return context


class AttractionListView(ListView):
    model = Attraction
    template_name = 'attractions/attraction_points_list.html'
    paginate_by = 10
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attractions'] = self.get_queryset().filter(area__slug=self.kwargs['slug'], is_active=True)
        return context
    
    
class AttractionDetailView(DetailView):
    model = Attraction
    template_name = 'attractions/attraction_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attraction'] = self.object
        return context