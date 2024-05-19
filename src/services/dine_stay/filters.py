import django_filters
from .models import Accommodation, Dining


class AccommodationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Accommodation
        fields = ['name', 'category', 'area']


class DinningFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Dining
        fields = ['name', 'area']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['name'].widget.attrs.update(
            {'class': 'form-control input-text', 'placeholder': 'Search here!'})
