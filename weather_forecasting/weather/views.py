import requests
from django.shortcuts import render
from datetime import datetime
from .models import Weather  # Import the Weather model

def weather_view(request):
    weather_data = None
    if request.method == 'POST':
        city = request.POST.get('city') 
        api_key = '3224be046b326ecc78fdb6b36467e0b0' 
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        # Make the API request
        response = requests.get(url).json()

        if response['cod'] == 200:
            # Create a new Weather instance
            weather = Weather.objects.create(
                city=response['name'],
                temperature=response['main']['temp'],
                max_temperature=response['main']['temp_max'],
                min_temperature=response['main']['temp_min'],
                humidity=response['main']['humidity'],
                latitude=response['coord']['lat'],
                longitude=response['coord']['lon']
            )
            weather_data = {
                'city': weather.city,
                'temperature': weather.temperature,
                'max_temp': weather.max_temperature,
                'min_temp': weather.min_temperature,
                'humidity': weather.humidity,
                'latitude': weather.latitude,
                'longitude': weather.longitude,
                'date_time': weather.date_time,
                'background_color': 'lightblue' if datetime.now().hour < 18 else 'darkblue',
            }
        else:
            weather_data = {'error': 'City not found'}

    return render(request, 'weather/weather.html', {'weather': weather_data})
