from django.shortcuts import render

# Create your views here.

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
    return render(request,'website/boqs.html')

def emergencyContact(request):
    return render(request,'website/emergencyContact.html')

def jurisdiction(request):
    return render(request, 'website/jurisdiction.html')

def buildingByeLaws(request):
    return render( request ,'website/buildingbyelaws.html')
