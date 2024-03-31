from django.apps import AppConfig


class ManagementAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.services.management'
    verbose_name = 'management'

    def ready(self):
        import src.services.management.signals
