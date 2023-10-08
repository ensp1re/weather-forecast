from . import models
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):


    class Meta:
        model = models.City
        fields = ["name"]
        widgets = {'name' : TextInput(attrs={
            'id' : 'city-input',
            'name' : 'city',
            'placeholder': 'Enter city'

         })}