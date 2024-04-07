from .models import Accommodation, Dining
from django.views.generic import ListView, DetailView

class AccommodationListView(ListView):
    model = Accommodation
    template_name = 'dine_stay/accommodations.html'
    context_object_name = 'accommodations'
    paginate_by = 10
    
    def get_queryset(self):
        accommodations = Accommodation.objects.filter(is_active=True)
        return accommodations

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accommodations'] = self.get_queryset()
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
    template_name = 'dine_stay/dinings.html'
    context_object_name = 'dinings'
    paginate_by = 10
    
    def get_queryset(self):
        dinings = Dining.objects.filter(is_active=True)
        return dinings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dinings'] = self.get_queryset()
        return context
    
    
class DiningDetailView(DetailView):
    model = Dining
    template_name = 'dine_stay/dining_details.html'
    context_object_name = 'dining'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dining = self.get_object()
        context['dining'] = dining
        context['dinings'] = Dining.objects.filter(is_active=True)
        
        return context
    
