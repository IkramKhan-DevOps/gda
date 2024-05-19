from django.views.generic import TemplateView

from .views import (

    NewsLetterCreateView,
    about, budget,
    teamDetails,
    act, department, departmentDetails,
    hotels, hotelsDetails, cafedetail,
    cafe, tenders,
    watertax,
    conservancytax,
    boqs, emergencyContact, jurisdiction, ContactView,
    watertax,
    conservancytax,
    boqs, emergencyContact, jurisdiction, ContactView,
    buildingByeLaws, HomeTemplateView
)

from django.urls import path

app_name = "website"

# OFFICIAL
urlpatterns = [
    path('newsletter/create/', NewsLetterCreateView.as_view(), name='newsletter-create'),
]

# UN OFFICIAL
urlpatterns += [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('budget/', budget, name='budget'),
    path('contact-us/', ContactView.as_view(), name='contact_us'),
    # path('team/', team, name='team'),
    path('teamDetails/', teamDetails, name='teamDetails'),
    path('act/', act, name='gda_act'),
    path('department/', department, name='departments'),
    path('departmentDetails/', departmentDetails, name='department_details'),
    path('hotels/', hotels, name='hotels'),
    path('hotelsdetails/', hotelsDetails, name='hotels_details'),
    path('tenders/', tenders, name='tenders'),
    path('cafe/', cafe, name='cafe'),
    path('cafedetail/', cafedetail, name='cafedetail'),
    path('watertax/', watertax, name='watertax'),
    path('conservancytax/', conservancytax, name='conservancytax'),
    path('propertytax/', TemplateView.as_view(template_name='website/property_tax.html'), name='propertytax'),
    path('boqs/', boqs, name='boqs'),
    path('emergency-contact/', emergencyContact, name='emergency_contact'),
    path('area-of-jurisdiction/', jurisdiction, name='jurisdiction'),
    path('building-bye-laws/', buildingByeLaws, name='building_bye_laws')
]
