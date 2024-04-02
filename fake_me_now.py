from random import sample

from django.contrib.sites.models import Site
from django.db import IntegrityError
from faker import Faker
from django.conf import settings
from core.settings import DOMAIN
from src.services.dinestay.models import (
    Accommodation, Type, DiningVenue)
from src.core.models import Country, NewsLetter
from src.services.events.models import (
    Event, EventType, Participant, Guest
)
from src.services.attractions.models import (
    Attraction, AttractionCategory, AttractionFeature
)
from src.services.management.models import Document, DocumentType
from src.services.users.models import User

fake = Faker()

""" HELPERS """


def __print_start(model):
    print()
    print(f"__ BUILD: {model} START __")


def __print_ended(model):
    print(f"__ BUILD: {model} ENDED __")
    print()


""" BASIC """


def basic_configuration():
    sites = Site.objects.all()

    # SITE SETTINGS
    if sites:
        sites = sites[0]
        sites.domain = DOMAIN
        sites.name = DOMAIN
        sites.save()
        print(f"---- Site domain updated to {sites.domain}")
    else:
        Site.objects.create(
            domain=DOMAIN,
            name=DOMAIN,
        )
        print(f"---- Site domain created to {DOMAIN}")


""" GLOBALS """


def country_fake():
    __print_start("Country")
    countries = [
        {
            'name': 'Pakistan',
            'short_name': 'PK',
            'language_code': 'ur_PK',
            'currency_code': 'PKR',
            'phone_code': '+92'
        },
    ]

    for country in countries:
        name = country['name']
        short_name = country['short_name']
        language_code = country['language_code']
        currency_code = country['currency_code']
        phone_code = country['phone_code']

        try:
            Country.objects.create(
                name=name, short_name=short_name, language=language_code,
                currency=currency_code,
                phone_code=phone_code
            )

            print(f"---- object: {country['name']} faked.")
        except IntegrityError as e:
            print(e.__str__())

    __print_ended("Country")


def load_newsletters():
    __print_start("NewsLetter")
    newsletters = [
        {"email": "mark@exarth.com"},
        {"email": "joseph@exarth.com"},
        {"email": "jane@exarth.com"},
        {"email": "john.smith@exarth.com"},
        {"email": "jane.doe@exarth.com"},
        {"email": "david.wilson@exarth.com"},
        {"email": "susan.jones@exarth.com"},
        {"email": "michael.brown@exarth.com"},
        {"email": "emily.williams@exarth.com"},
        {"email": "robert.davis@exarth.com"},
        {"email": "lisa.johnson@exarth.com"},
        {"email": "matthew.miller@exarth.com"},
    ]

    for newsletter_data in newsletters:
        email = newsletter_data["email"]

        try:
            NewsLetter.objects.create(
                email=email,
            )

            print(f"---- object: {email} created.")
        except IntegrityError as e:
            print(e.__str__())

    __print_ended("NewsLetter")


""" MANAGEMENT APP """


def document_type_fake():
    __print_start("Document Type")
    document_types = [
        {"name": "Policy"},
        {"name": "Terms & Conditions"},
        {"name": "Privacy Policy"},
        {"name": "User Manual"},
    ]

    for document_type_data in document_types:
        name = document_type_data["name"]

        try:
            DocumentType.objects.create(
                name=name,
            )

            print(f"---- object: {name} created.")
        except IntegrityError as e:
            print(e.__str__())

    __print_ended("Document Type")


def document_fake():
    __print_start("Document")
    documents = [
        {"title": "Policy", "document_type": "Policy", "description": "Policy description"},
        {"title": "Terms & Conditions", "document_type": "Terms & Conditions",
         "description": "Terms & Conditions description"},
        {"title": "Privacy Policy", "document_type": "Privacy Policy", "description": "Privacy Policy description"},
        {"title": "User Manual", "document_type": "User Manual", "description": "User Manual description"},
    ]

    for i in range(10):
        title = fake.sentence()
        document_type = DocumentType.objects.order_by('?').first()
        description = fake.paragraph()
        is_active = True

        try:
            Document.objects.create(
                title=title,
                document_type=document_type,
                description=description,
                is_active=is_active,
            )

            print(f"---- object: {title} created.")
        except IntegrityError as e:
            print(e.__str__())

    __print_ended("Document")


""" EVENTS APP """


def event_type_fake():
    __print_start("Event Type")
    event_types = [
        {"name": "Webinar", "description": "Webinar description"},
        {"name": "Workshop", "description": "Workshop description"},
        {"name": "Seminar", "description": "Seminar description"},
        {"name": "Conference", "description": "Conference description"},
    ]

    for event_type_data in event_types:
        name = event_type_data["name"]
        description = event_type_data["description"]

        try:
            EventType.objects.create(
                name=name,
                description=description,
            )

            print(f"---- object: {name} created.")
        except IntegrityError as e:
            print(e.__str__())

    __print_ended("Event Type")


def event_fake():
    __print_start("Event")
    events = [
        {"name": "Webinar", "event_type": "Webinar", "description": "Webinar description"},
        {"name": "Workshop", "event_type": "Workshop", "description": "Workshop description"},
        {"name": "Seminar", "event_type": "Seminar", "description": "Seminar description"},
        {"name": "Conference", "event_type": "Conference", "description": "Conference description"},
    ]

    for i in range(10):
        name = fake.sentence()
        event_type = EventType.objects.order_by('?').first()
        description = fake.paragraph()
        start_date = fake.date_time_this_year()
        end_date = fake.date_time_this_year()
        location = fake.address()
        latitude = fake.latitude()
        longitude = fake.longitude()
        is_active = True

        try:
            Event.objects.create(
                name=name,
                event_type=event_type,
                description=description,
                start_date=start_date,
                end_date=end_date,
                location=location,
                latitude=latitude,
                longitude=longitude,
                is_active=is_active,
            )

            print(f"---- object: {name} created.")
        except IntegrityError as e:
            print(e.__str__())

    __print_ended("Event")


def participant_fake():
    __print_start("Participant")
    participants = [
        {"full_name": "Adam Williams", "email": "adam.williams@example.com", "phone_number": "+1234567890",
         "address": "321 Maple Street, Smalltown"},
        {"full_name": "Emma Taylor", "email": "emma.taylor@example.com", "phone_number": "+1987654321",
         "address": "654 Birch Lane, Suburbia"},
        {"full_name": "David Martinez", "email": "david.martinez@example.com", "phone_number": "+1555098765",
         "address": "987 Cedar Avenue, Metropolis"},
        {"full_name": "Olivia Johnson", "email": "olivia.johnson@example.com", "phone_number": "+1770321654",
         "address": "111 Oak Street, Megacity"},
        {"full_name": "Benjamin Wilson", "email": "benjamin.wilson@example.com", "phone_number": "+1234567890",
         "address": "456 Elm Avenue, Anytown"},
        {"full_name": "Sophia Garcia", "email": "sophia.garcia@example.com", "phone_number": "+1987654321",
         "address": "789 Pine Street, Suburbia"},
        {"full_name": "Ethan Rodriguez", "email": "ethan.rodriguez@example.com", "phone_number": "+1555098765",
         "address": "123 Oak Lane, Metropolis"},
        {"full_name": "Isabella Brown", "email": "isabella.brown@example.com", "phone_number": "+1770321654",
         "address": "789 Maple Road, Megacity"},
        {"full_name": "Liam Moore", "email": "liam.moore@example.com", "phone_number": "+1234567890",
         "address": "101 Cedar Street, Anytown"},
        {"full_name": "Ava Lopez", "email": "ava.lopez@example.com", "phone_number": "+1987654321",
         "address": "222 Elm Lane, Suburbia"},
        {"full_name": "Mason Lee", "email": "mason.lee@example.com", "phone_number": "+1555098765",
         "address": "333 Pine Avenue, Metropolis"},
        {"full_name": "Sophia Hernandez", "email": "sophia.hernandez@example.com", "phone_number": "+1770321654",
         "address": "444 Oak Road, Megacity"},
        {"full_name": "Logan Thompson", "email": "logan.thompson@example.com", "phone_number": "+1234567890",
         "address": "555 Maple Lane, Anytown"},
        {"full_name": "Mia Nelson", "email": "mia.nelson@example.com", "phone_number": "+1987654321",
         "address": "666 Elm Road, Suburbia"},
        {"full_name": "James Carter", "email": "james.carter@example.com", "phone_number": "+1555098765",
         "address": "777 Pine Street, Metropolis"},
        {"full_name": "Emma Baker", "email": "emma.baker@example.com", "phone_number": "+1770321654",
         "address": "888 Oak Lane, Megacity"},
        {"full_name": "Noah Hall", "email": "noah.hall@example.com", "phone_number": "+1234567890",
         "address": "999 Cedar Avenue, Anytown"},
        {"full_name": "Ava King", "email": "ava.king@example.com", "phone_number": "+1987654321",
         "address": "1010 Maple Street, Suburbia"},
        {"full_name": "Liam Powell", "email": "liam.powell@example.com", "phone_number": "+1555098765",
         "address": "1111 Elm Lane, Metropolis"},
        {"full_name": "Charlotte Young", "email": "charlotte.young@example.com", "phone_number": "+1770321654",
         "address": "1212 Pine Avenue, Megacity"}
    ]

    for i in range(10):
        full_name = fake.name()
        email = fake.email()
        phone_number = fake.phone_number()
        address = fake.address()

        try:
            Participant.objects.create(
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                address=address,
                event=Event.objects.order_by('?').first(),
            )

            print(f"---- object: {full_name} created.")
        except IntegrityError as e:
            print(e.__str__())


def guest_fake():
    __print_start("Guest")
    guests = [
        {"full_name": "John Doe", "email": "john.doe@example.com", "phone_number": "+1234567890",
         "designation": "Manager"},
        {"full_name": "Jane Smith", "email": "jane.smith@example.com", "phone_number": "+1987654321",
         "designation": "Coordinator"},
        {"full_name": "Michael Johnson", "email": "michael.johnson@example.com", "phone_number": "+1555098765",
         "designation": "Supervisor"},
        {"full_name": "Emily Brown", "email": "emily.brown@example.com", "phone_number": "+1770321654",
         "designation": "Assistant"},
        {"full_name": "David Williams", "email": "david.williams@example.com", "phone_number": "+1234567890",
         "designation": "Director"},
        {"full_name": "Sophia Rodriguez", "email": "sophia.rodriguez@example.com", "phone_number": "+1987654321",
         "designation": "Analyst"},
        {"full_name": "Daniel Martinez", "email": "daniel.martinez@example.com", "phone_number": "+1555098765",
         "designation": "Consultant"},
        {"full_name": "Olivia Garcia", "email": "olivia.garcia@example.com", "phone_number": "+1770321654",
         "designation": "Developer"},
        {"full_name": "William Brown", "email": "william.brown@example.com", "phone_number": "+1234567890",
         "designation": "Engineer"},
        {"full_name": "Emma Davis", "email": "emma.davis@example.com", "phone_number": "+1987654321",
         "designation": "Designer"}
    ]

    for i in range(10):
        full_name = fake.name()
        email = fake.email()
        phone_number = fake.phone_number()
        designation = fake.job()

        try:
            Guest.objects.create(
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                designation=designation,
                event=Event.objects.order_by('?').first(),
            )

            print(f"---- object: {full_name} created.")
        except IntegrityError as e:
            print(e.__str__())


"""" ATTRACTION APP """


def attraction_feature_fake():
    __print_start("Attraction Feature")
    attraction_features = [
        {"name": "Cafe"},
        {"name": "Bar"},
        {"name": "Restaurant"},
        {"name": "Park"},
        {"name": "Museum"},
        {"name": "Zoo"},
        {"name": "Beach"},
        {"name": "Shopping Mall"},
        {"name": "Amusement Park"},
        {"name": "Theater"},
        {"name": "Cinema"},
        {"name": "Library"},
        {"name": "Gym"},
        {"name": "Spa"},
        {"name": "Salon"},
        {"name": "Hotel"},
        {"name": "Resort"},
        {"name": "Motel"},
        {"name": "Inn"},
    ]

    for attraction_feature_data in attraction_features:
        name = attraction_feature_data["name"]

        try:
            AttractionFeature.objects.create(
                name=name,
            )

            print(f"---- object: {name} created.")
        except IntegrityError as e:
            print(e.__str__())

    __print_ended("Attraction Feature")


def attraction_category_fake():
    __print_start("Attraction Category")
    attraction_categories = [
        {"name": "Museum"},
        {"name": "Park"},
        {"name": "Zoo"},
        {"name": "Beach"},
        {"name": "Shopping Mall"},
        {"name": "Amusement Park"},
        {"name": "Theater"},
        {"name": "Cinema"},
        {"name": "Library"},
        {"name": "Gym"},
        {"name": "Spa"},
        {"name": "Salon"},
    ]

    for attraction_category_data in attraction_categories:
        name = attraction_category_data["name"]

        try:
            AttractionCategory.objects.create(
                name=name,
            )

            print(f"---- object: {name} created.")
        except IntegrityError as e:
            print(e.__str__())

    __print_ended("Attraction Category")


def attraction_fake():
    __print_start("Attraction")
    attractions = [
        {"name": "John X Museum"},
        {"name": "Jane Y Park"},
        {"name": "Michael Z Zoo"},
        {"name": "Emily A Beach"},
        {"name": "David B Shopping Mall"},
        {"name": "Sophia C Amusement Park"},
        {"name": "Daniel D Theater"},
        {"name": "Olivia E Cinema"},
        {"name": "William F Library"},
        {"name": "Emma G Gym"},
        {"name": "Noah H Spa"},
        {"name": "Ava I Salon"},
        {"name": "Liam J Hotel"},
        {"name": "Charlotte K Resort"},
        {"name": "Mia L Motel"},
        {"name": "James M Inn"},
    ]

    for attraction in attractions:
        name = attraction["name"]
        category = AttractionCategory.objects.order_by('?').first()
        description = fake.paragraph()
        address = fake.address()
        latitude = fake.latitude()
        longitude = fake.longitude()
        thumbnail = fake.image_url()
        video = fake.url()
        features = sample(list(AttractionFeature.objects.all()), k=5)

        try:
            attraction = Attraction.objects.create(
                name=name,
                category=category,
                description=description,
                address=address,
                latitude=latitude,
                longitude=longitude,
                thumbnail=thumbnail,
                video=video,
            )
            attraction.features.add(*features)

            print(f"---- object: {name} created.")
        except IntegrityError as e:
            print(e.__str__())

    __print_ended("Attraction")


""" DINE STAY APP """


def type_fake():
    __print_start("Type")
    types = [
        {"name": "Hotel", "image": "Hotel image"},
        {"name": "Resort", "image": "Resort image"},
        {"name": "Motel", "image": "Motel image"},
        {"name": "Inn", "image": "Inn image"},
    ]

    for type_data in types:
        name = type_data["name"]
        image = type_data["image"]

        try:
            Type.objects.create(
                name=name,
                image=image,
            )

            print(f"---- object: {name} created.")
        except IntegrityError as e:
            print(e.__str__())

    __print_ended("Type")


def accommodation_fake():
    __print_start("Accommodation")
    accommodations = [
        {"name": "Hotel", "description": "Hotel description", "thumbnail": "Hotel thumbnail", "video": "Hotel video",
         "content": "Hotel content", "stay_type": "Hotel", "phone": "+1234567890", "email": "guest1@gmail.com", "website": "www.hotel.com", "address": "Hotel address", "lat": "Hotel lat", "lon": "Hotel lon"},
        {"name": "Resort", "description": "Resort description", "thumbnail": "Resort thumbnail", "video": "Resort video", "content": "Resort content", "stay_type": "Resort", "phone": "+1987654321", "email": "Hotel@gmail.com" , "website": "www.resort.com", "address": "Resort address", "lat": "Resort lat", "lon": "Resort lon"},
    ] 
    for i in range(10):
        name = fake.sentence()
        description = fake.paragraph()
        thumbnail = fake.image_url()
        video = fake.url()
        content = fake.paragraph()
        stay_type = Type.objects.order_by('?').first()
        phone = fake.phone_number()
        email = fake.email()
        website = fake.url()
        address = fake.address()
        lat = fake.latitude()
        lon = fake.longitude()

        try:
            Accommodation.objects.create(
                name=name,
                description=description,
                thumbnail=thumbnail,
                video=video,
                content=content,
                stay_type=stay_type,
                phone=phone,
                email=email,
                website=website,
                address=address,
                lat=lat,
                lon=lon,
            )

            print(f"---- object: {name} created.")
        except IntegrityError as e:
            print(e.__str__())
            
    __print_ended("Accommodation")
    
    
def dining_venue_fake():
    __print_start("Dining Venue")
    dining_venues = [
        {"name": "Restaurant", "description": "Restaurant description", "thumbnail": "Restaurant thumbnail", "video": "Restaurant video", "content": "Restaurant content", "dine_type": "Restaurant", "phone": "+1234567890", "email": "alpiune@gmail.com" , "website": "www.restaurant.com", "address": "Restaurant address", "lat": "Restaurant lat", "lon": "Restaurant lon"},
        {"name": "Cafe", "description": "Cafe description", "thumbnail": "Cafe thumbnail", "video": "Cafe video", "content": "Cafe content", "dine_type": "Cafe", "phone": "+1987654321", "email": "sweetTooth@gmail.com", "website": "www.cafe.com", "address": "Cafe address", "lat": "Cafe lat", "lon": "Cafe lon"},
    ]
    
    for i in range(10):
        name = fake.sentence()
        description = fake.paragraph()
        thumbnail = fake.image_url()
        video = fake.url()
        content = fake.paragraph()
        dine_type = Type.objects.order_by('?').first()
        phone = fake.phone_number()
        email = fake.email()
        website = fake.url()
        address = fake.address()
        lat = fake.latitude()
        lon = fake.longitude()

        try:
            DiningVenue.objects.create(
                name=name,
                description=description,
                thumbnail=thumbnail,
                video=video,
                content=content,
                dine_type=dine_type,
                phone=phone,
                email=email,
                website=website,
                address=address,
                lat=lat,
                lon=lon,
            )

            print(f"---- object: {name} created.")
        except IntegrityError as e:
            print(e.__str__())
        
    __print_ended("Dining Venue")    

    
def main():
    # basic_configuration()
    #
    # country_fake()
    # load_newsletters()
    #
    # document_type_fake()
    # document_fake()
    #
    # event_type_fake()
    # event_fake()
    # participant_fake()
    # guest_fake()
    # accommodation_fake()
    # type_fake()
    # dining_venue_fake()

    attraction_feature_fake()
    attraction_category_fake()
    attraction_fake()


if __name__ == '__main__':
    main()
