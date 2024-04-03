from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from src.core.models import NewsLetter

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


def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


def budget(request):
    return render(request, 'website/budget.html')


def contactUs(request):
    return render(request, 'website/contactUs.html')


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


def cafe(request):
    return render(request, 'website/cafe.html')


def cafedetail(request):
    return render(request, 'website/cafedetail.html')


def event(request):
    return render(request, 'website/events.html')


def eventdetail(request):
    return render(request, 'website/eventdetails.html')


def watertax(request):
    return render(request, 'website/watertax.html')


def conservancytax(request):
    return render(request, 'website/conservancytax.html')


def propertytax(request):
    return render(request, 'website/property_tax.html')


def attractions(request):
    return render(request, 'website/attraction.html')


def attractionlist(request):
    return render(request, 'website/attractionlist.html')


def attractiondetail(request):
    return render(request, 'website/attractiondetail.html')


def boqs(request):
    return render(request, 'website/boqs.html')


def emergencyContact(request):
    return render(request, 'website/emergencyContact.html')


def jurisdiction(request):
    return render(request, 'website/jurisdiction.html')


def buildingByeLaws(request):
    return render(request, 'website/buildingbyelaws.html')
