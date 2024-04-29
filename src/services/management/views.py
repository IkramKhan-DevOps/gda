from django.core.paginator import Paginator
from django.views.generic import ListView

from src.services.management.models import Document


class DocumentListView(ListView):
    model = Document
    template_name = 'management/download_list.html'

    def get_context_data(self, **kwargs):
        context = super(DocumentListView, self).get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), 10)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context['object_list'] = page_object
        return context
