from django.views.generic import ListView, DetailView
from .models import Department, Directors


class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/departments.html'
    context_object_name = 'departments'
    paginate_by = 10
    
    def get_queryset(self):
        departments = Department.objects.filter(is_active=True)
        for department in departments:
            department.director = Directors.objects.filter(department=department).first()
        return departments

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = self.get_queryset()
        return context


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/department_details.html'
    context_object_name = 'department'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department = self.get_object()
        context['department'] = department
        context['departments'] = Department.objects.filter(is_active=True)
        context['director'] = Directors.objects.filter(department=department).first()
        
        return context


class DirectorListView(ListView):
    model = Directors
    template_name = 'departments/directors.html'
    context_object_name = 'directors'
    paginate_by = 10
    
    def get_queryset(self):
        directors = Directors.objects.filter(is_active=True)
        for director in directors:
            director.department = Department.objects.filter(directors=director).first()
        return directors

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directors'] = self.get_queryset()
        return context
