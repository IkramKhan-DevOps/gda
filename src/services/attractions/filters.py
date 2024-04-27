import django_filters

from src.services.attractions.models import AttractionArea, Attraction


class AttractionAreaFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = AttractionArea
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['name'].widget.attrs.update(
            {'class': 'form-control input-text', 'placeholder': 'Enter Attraction Area Name'})


class AttractionPointFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Attraction
        fields = ['name','category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['name'].widget.attrs.update(
            {'class': 'form-control input-text', 'placeholder': 'Enter Attraction Area Name'})


