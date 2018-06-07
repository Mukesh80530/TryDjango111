from django.forms import ModelForm
from .models import RestaurantLocation


class RestaurantLocationForm(ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = ['name', 'location', 'category']