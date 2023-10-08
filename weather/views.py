from django.shortcuts import render
from django.http import HttpResponse
import requests
from . import models
from . import forms

api_key = 'b0da1c89f6744d0ff405beaff0f3def8'

def index(request):
    api_key = 'b0da1c89f6744d0ff405beaff0f3def8'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + api_key


    if (request.method == "POST"):
        form = forms.CityForm(request.POST)
        form.save()


    form = forms.CityForm() # для очистки форми після перезавантаження
    cities = models.City.objects.all()

    all_cities = list()

    for city in cities:
        try:
            response = requests.get(url.format(city))

            if response.status_code == 200:
               weather = response.json()
            else:
                weather = "Error"
            city_info = {
                "city": city,
                "temp": int(round(float(weather["main"]["temp"]) - float(273.15), 0)),
                "icon": weather["weather"][0]["icon"]

            }

            all_cities.append(city_info)
        except (Exception, TypeError) as e:
            city_info = {
                "city": city,
                "temp": "TRY AGAIN!",
                "icon": ""

            }
            all_cities.append(city_info)
            pass


    context = {"all_info" : all_cities, "form" : form}


    return render(request, 'weather/index.html', context)