from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .filters import DepartmentFilter
from .models import Chairman, Department, DirectorGeneral, Directors, Personnel


class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/departments.html'

    def get_queryset(self):
        departments = Department.objects.filter(is_active=True)
        for department in departments:
            department.director = Directors.objects.filter(department=department).first()
        return departments

    def get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        _filter = DepartmentFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_form'] = _filter.form
        paginator = Paginator(_filter.qs, 20)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context['object_list'] = page_object
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


class PersonalsView(ListView):
    template_name = 'departments/team.html'

    def get(self, request, *args, **kwargs):
        chairmen = Chairman.objects.filter(is_active=True)
        director_generals = DirectorGeneral.objects.filter(is_active=True)
        directors = Directors.objects.filter(is_active=True)

        team_members = {
            'chairmen': chairmen,
            'director_generals': director_generals,
            'directors': directors,
        }

        return render(request, self.template_name, team_members)
