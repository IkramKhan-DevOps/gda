from django.apps import AppConfig


class EventAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.services.events'
    verbose_name = 'Events'

    def ready(self):
        import src.services.events.signals
