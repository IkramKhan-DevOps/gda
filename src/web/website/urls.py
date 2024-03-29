from .views import (
    home, about, budget,
    team, teamDetails,
    act, department, departmentDetails,
    hotels, hotelsDetails, cafedetail,
    cafe, tenders, event,
    eventdetail, watertax,
    conservancytax, propertytax,
    attractions, attractionlist, attractiondetail,
    boqs, emergencyContact, jurisdiction, contactUs,
    buildingByeLaws
)

from django.urls import path

app_name = "website"
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('budget/', budget, name='budget'),
    path('contact-us/', contactUs, name='contact_us'),
    path('team/', team, name='team'),
    path('teamDetails/', teamDetails, name='teamDetails'),
    path('act/', act, name='gda_act'),
    path('department/', department, name='departments'),
    path('departmentDetails/', departmentDetails, name='department_details'),
    path('hotels/', hotels, name='hotels'),
    path('hotelsdetails/', hotelsDetails, name='hotels_details'),
    path('tenders/', tenders, name='tenders'),
    path('cafe/', cafe, name='cafe'),
    path('cafedetail/', cafedetail, name='cafedetail'),
    path('event/', event, name='event'),
    path('eventdetail/', eventdetail, name='eventdetail'),
    path('watertax/', watertax, name='watertax'),
    path('conservancytax/', conservancytax, name='conservancytax'),
    path('propertytax/', propertytax, name='propertytax'),
    path('attractions/', attractions, name='attractions'),
    path('attractionlist/', attractionlist, name='attractionlist'),
    path('attractiondetail/', attractiondetail, name='attractiondetail'),
    path('boqs/', boqs, name='boqs'),
    path('emergency-contact/', emergencyContact, name='emergency_contact'),
    path('area-of-jurisdiction/', jurisdiction, name='jurisdiction'),
    path('building-bye-laws/', buildingByeLaws, name='building_bye_laws')
]
