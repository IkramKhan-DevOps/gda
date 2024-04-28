import django_filters
from src.services.events.models import Event


class EventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['name','event_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['name'].widget.attrs.update(
            {'class': 'form-control input-text', 'placeholder': 'Enter Event Name'})




