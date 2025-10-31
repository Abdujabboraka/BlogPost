from django.shortcuts import render
from blog.models import BlogCategory, Blog
import requests
from django.db.models import Count
# Create your views here.

url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
try:
    response = requests.get(url)
    data = response.json()
    dollar = data[0]['Rate']
    ruble = data[1]['Rate']
except:
    dollar = 0
    ruble = 0

# weather/utils.py
import requests

def get_weather(city_name):
    """Fetch current weather for a given city from WeatherAPI."""
    api_key = "bc6ead79290b4cf1bf592549252010"
    endpoint = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city_name,
        "aqi": "no"
    }

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()

        # Simplify data for template
        return {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "temp_c": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
            "icon": data["current"]["condition"]["icon"],
            "wind_kph": data["current"]["wind_kph"],
            "humidity": data["current"]["humidity"]
        }

    except Exception as e:
        print("Error fetching weather:", e)
        return None

# getting top five blogs
top5 = Blog.objects.annotate(likescount=Count('likes')).order_by('-likes')[:5]
random_blogs = Blog.objects.annotate(likescount=Count('likes')).order_by('likes')[:5]

def homepage(request):
    categories = BlogCategory.objects.all()
    blogs = Blog.objects.all()
    weather = get_weather("Tashkent")

    context = {
        'sum': "OZBEKISTON",
        'dollar': dollar,
        'ruble': ruble,
        'weather': weather,
        'categories': categories,
        'blogs': blogs,
        'top5' : top5,
        'random_blogs': random_blogs

    }
    return render(request, 'homepage/homepage.html', context)

