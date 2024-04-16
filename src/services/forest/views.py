from django.views.generic import ListView, DetailView
from .models import Greenery, Wildlife, WildlifeType, GreeneryType

#done
class WildlifeListView(ListView):
    model = Wildlife
    template_name = 'forest/wildlife.html'
    context_object_name = 'wildlife_list'
    paginate_by = 6
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_queryset(self):
        return Wildlife.objects.filter(is_active=True)
    
    
class WildlifeDetailView(DetailView):
    model = Wildlife
    template_name = 'forest/wildlife_detail.html'
    context_object_name = 'wildlife_details'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        wildlife = self.get_object()
        context['wildlife_details'] = wildlife
        return context


#done
class WildlifeTypeListView(ListView):
    model = WildlifeType
    template_name = 'forest/wildlife_type.html'
    paginate_by = 6
    context_object_name = 'wildlife_types'
    
    def get_queryset(self):
        return WildlifeType.objects.all()    


class GreeneryListView(ListView):
    model = Greenery
    template_name = 'forest/greenery_list.html'
    context_object_name = 'greenery_list'
    paginate_by = 6
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_queryset(self):
        return Greenery.objects.filter(is_active=True)
    
    
class GreeneryDetailView(DetailView):
    model = Greenery
    template_name = 'forest/greenery_detail.html'
    context_object_name = 'greenery_details'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    
class GreeneryTypeListView(ListView):
    model = GreeneryType
    template_name = 'forest/greenery_type.html'
    context_object_name = 'greenery_types'
    paginate_by = 6
    
    def get_queryset(self):
        return GreeneryType.objects.all()
    