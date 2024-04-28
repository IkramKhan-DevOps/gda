from django.apps import AppConfig


class AttractionAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.services.attractions'
    verbose_name = 'Attractions'

    # def ready(self):
    #     import src.services.events.signals
