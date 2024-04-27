from django.apps import AppConfig


class WeatherAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.services.weather'
    verbose_name = 'Weather'

    