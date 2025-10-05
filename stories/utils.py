import requests
from datetime import datetime
from .models import NasaAPOD

NASA_API_KEY = 'PLZGcNZIGj6kGqUhJ03RBltaIZxZdbIwAGR5yp7y'  # Replace with your key

def fetch_nasa_apod():
    url = f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Save to database
        apod, created = NasaAPOD.objects.update_or_create(
            date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
            defaults={
                'title': data['title'],
                'explanation': data['explanation'],
                'url': data['url'],
                'media_type': data['media_type'],
            }
        )
        return apod
    else:
        print("Error fetching NASA APOD:", response.status_code)
        return None
