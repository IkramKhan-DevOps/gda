from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from src.web.accounts.forms import IncompleteServiceProviderForm, UserForm

from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from src.web.service_provider.models import ServiceProvider


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'agency/dashboard.html'


@method_decorator(login_required, name='dispatch')
class OrdersView(TemplateView):
    template_name = 'agency/orders.html'


@method_decorator(login_required, name='dispatch')
class TravellersView(TemplateView):
    template_name = 'agency/travellers.html'


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'agency/profile.html'


@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    template_name = 'service_provider/edit_profile.html'
    form_class = IncompleteServiceProviderForm

    def get(self, request):
        user = request.user
        agency_instance = get_object_or_404(ServiceProvider, owner=user)
        form = self.form_class(instance=agency_instance)
        return render(request, template_name=self.template_name, context={"form": form})

    def post(self, request):
        user = request.user
        agency_instance = get_object_or_404(ServiceProvider, owner=user)
        form = self.form_class(request.POST, request.FILES, instance=agency_instance)
        if form.is_valid():
            form.save()
            return render(request, template_name=self.template_name, context={"form": form})
        else:
            return render(request, template_name=self.template_name, context={"form": form})


@method_decorator(login_required, name='dispatch')
class ReviewsView(TemplateView):
    template_name = 'service_provider/reviews.html'


@method_decorator(login_required, name='dispatch')
class WishlistView(TemplateView):
    template_name = 'service_provider/wishlist.html'


@method_decorator(login_required, name='dispatch')
class TravelAgentsView(TemplateView):
    template_name = 'service_provider/travel_agents.html'


@method_decorator(login_required, name='dispatch')
class InvoicesView(TemplateView):
    template_name = 'service_provider/invoices.html'


@method_decorator(login_required, name='dispatch')
class PaymentsView(TemplateView):
    template_name = 'service_provider/payments.html'


@method_decorator(login_required, name='dispatch')
class CurrencyView(TemplateView):
    template_name = 'service_provider/currency.html'


@method_decorator(login_required, name='dispatch')
class SubscriberView(TemplateView):
    template_name = 'service_provider/subscriber.html'


@method_decorator(login_required, name='dispatch')
class LocationView(TemplateView):
    template_name = 'service_provider/location.html'


@method_decorator(login_required, name='dispatch')
class SettingView(View):
    template_name = 'service_provider/setting.html'
    form = UserForm

    def get(self, request):
        form = self.form(instance=request.user)
        return render(request, template_name=self.template_name, context={"form": form})

    def post(self, request):
        form = self.form(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Updated Successfully')
            return redirect('service_provider:setting')
        else:
            messages.error(request, "Error While Updating")
            return render(request, template_name=self.template_name, context={"form": form})
