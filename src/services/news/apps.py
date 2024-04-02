from django.apps import AppConfig


class NewsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.services.news'
    verbose_name = 'News'

    def ready(self):
        import src.services.events.signals
