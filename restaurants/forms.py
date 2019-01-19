from django.forms import ModelForm
from .models import RestaurantLocation
from django import forms


class RestaurantLocationForm(ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = ['name', 'location', 'category']

class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)