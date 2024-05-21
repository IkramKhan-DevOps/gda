import openmeteo_requests
import requests_cache
from retry_requests import retry

from src.services.management.models import WeatherLocation

cache_session = requests_cache.CachedSession('.cache', expire_after=30)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)
url = "https://api.open-meteo.com/v1/forecast"

def get_galiyat_weather():
    location = WeatherLocation.objects.first()
    if not location:
        latitude = 34.07
        longitude = 73.38
    else:
        latitude = location.latitude
        longitude = location.longitude
        
    params = {
        "latitude": latitude ,
        "longitude": longitude,
        "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "is_day", "precipitation", "rain",
                    "showers", "snowfall", "weather_code", "cloud_cover", "pressure_msl", "surface_pressure",
                    "wind_speed_10m"]
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    # Current values. The order of variables needs to be the same as requested.
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_relative_humidity_2m = current.Variables(1).Value()
    current_apparent_temperature = current.Variables(2).Value()
    current_is_day = current.Variables(3).Value()
    current_precipitation = current.Variables(4).Value()
    current_rain = current.Variables(5).Value()
    current_showers = current.Variables(6).Value()
    current_snowfall = current.Variables(7).Value()
    current_weather_code = current.Variables(8).Value()
    current_cloud_cover = current.Variables(9).Value()
    current_pressure_msl = current.Variables(10).Value()
    current_surface_pressure = current.Variables(11).Value()
    current_wind_speed_10m = current.Variables(12).Value()

    return {
        "current_time": current.Time(),
        "current_temperature_2m": current_temperature_2m,
        "current_relative_humidity_2m": current_relative_humidity_2m,
        "current_apparent_temperature": current_apparent_temperature,
        "current_is_day": current_is_day,
        "current_precipitation": current_precipitation,
        "current_rain": current_rain,
        "current_showers": current_showers,
        "current_snowfall": current_snowfall,
        "current_weather_code": current_weather_code,
        "current_cloud_cover": current_cloud_cover,
        "current_pressure_msl": current_pressure_msl,
        "current_surface_pressure": current_surface_pressure,
        "current_wind_speed_10m": current_wind_speed_10m
    }
