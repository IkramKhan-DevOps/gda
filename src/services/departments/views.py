from django.views.generic import ListView
from .models import Department


class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/departments.html'
    context_object_name = 'departments'
    paginate_by = 10
    
    def get_queryset(self):
        return Department.objects.filter(is_active=True)
