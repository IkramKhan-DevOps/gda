
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from src.core.models import NewsLetter
from .models import Visit
from django.views.generic.edit import CreateView
from ...services.feedback.forms import ContactForm
from ...apps.weather.bll import get_galiyat_weather
from ...services.attractions.models import Attraction, AttractionArea
from ...services.departments.models import Directors, DirectorGeneral, Chairman
from ...services.dine_stay.models import Accommodation, Dining
from ...services.management.models import HomeSlider, GalleryImage

""" OFFICIAL """


class NewsLetterCreateView(View):

    def post(self, request):
        email = request.POST.get('email')

        # Check if email is provided
        if not email:
            messages.error(request, 'Please provide your email address.')
            return redirect(request.META.get('HTTP_REFERER'))

        # Check if email is already subscribed
        if NewsLetter.objects.filter(email=email).exists():
            messages.error(request, f"{email} you have already subscribed to our newsletter.")
            return redirect(request.META.get('HTTP_REFERER'))

        # Save email to database
        NewsLetter.objects.create(email=email)
        messages.success(request, 'You have successfully subscribed to our newsletter.')
        return redirect(request.META.get('HTTP_REFERER'))


""" UN-OFFICIAL """


def format_visit_count(count):
    if count < 1000:
        return str(count)
    elif count < 1000000:
        return f"{count // 1000}k"
    elif count < 1000000000:
        return f"{count // 1000000}M"
    else:
        return f"{count // 1000000000}B"


class HomeTemplateView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weather_data'] = get_galiyat_weather(self)
        context['top_attractions'] = AttractionArea.objects.all()[:10]
        context['restaurant'] = Accommodation.objects.all()[:10]
        context['dinning'] = Dining.objects.all()[:10]

        context['chairman'] = Chairman.objects.order_by('-created_at').first()
        context['director'] = Directors.objects.all()[:5]
        context['director_general'] = DirectorGeneral.objects.all()[:5]
        context['home_slider'] = HomeSlider.objects.all()

        visit_count = Visit.objects.first()

        if not visit_count:
            visit_count = Visit.objects.create(count=0)

        visit_count.count += 1
        visit_count.save()

        formatted_count = format_visit_count(visit_count.count)
        context['formatted_count'] = formatted_count
        return context


def about(request):
    return render(request, 'website/about.html')


def budget(request):
    return render(request, 'website/budget.html')


class ContactView(CreateView):
    template_name = 'website/contactUs.html'
    form_class = ContactForm
    success_url = reverse_lazy('website:contact_us')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your message has been sent successfully!")
        return response


class ForestView(TemplateView):
    template_name = 'website/forest.html'


def team(request):
    return render(request, 'website/team.html')


def teamDetails(request):
    return render(request, 'website/teamDetails.html')


def act(request):
    return render(request, 'website/gda_act.html')


def department(request):
    return render(request, 'website/departments.html')


def departmentDetails(request):
    return render(request, 'website/departments_details.html')


def hotels(request):
    return render(request, 'website/hotels.html')


def hotelsDetails(request):
    return render(request, 'website/hotels_details.html')


def tenders(request):
    return render(request, 'website/tenders.html')


class GalleryImageView(ListView):
    model = GalleryImage
    template_name = 'website/gallery.html'
    context_object_name = 'images'


def cafe(request):
    return render(request, 'website/cafe.html')


def cafedetail(request):
    return render(request, 'website/cafedetail.html')


def watertax(request):
    return render(request, 'website/watertax.html')


def conservancytax(request):
    return render(request, 'website/conservancytax.html')


def boqs(request):
    return render(request, 'website/boqs.html')


def emergencyContact(request):
    return render(request, 'website/emergencyContact.html')


def jurisdiction(request):
    return render(request, 'website/jurisdiction.html')


def buildingByeLaws(request):
    return render(request, 'website/buildingbyelaws.html')
