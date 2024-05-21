import django_filters

from src.services.forest.models import Greenery,  Wildlife


class WildLifeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Wildlife
        fields = ['name','scientific_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['name'].widget.attrs.update(
            {'class': 'form-control input-text', 'placeholder': 'Enter Wild Life Name'})


class GreeneryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Greenery
        fields = ['name','scientific_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['name'].widget.attrs.update(
            {'class': 'form-control input-text', 'placeholder': 'Enter plant or tree Name'})


