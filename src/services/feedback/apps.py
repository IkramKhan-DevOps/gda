from django.apps import AppConfig


class FeedbackAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.services.feedback'
    verbose_name = 'Feedback'

    def ready(self):
        import src.services.management.signals
