from django.forms import ModelForm
from .models import RestaurantLocation
from django import forms
from .validators import validate_email, validate_category

class RestaurantLocationDjangoForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'hello' or 'Hello':
            raise forms.ValidationError("Not a valid name")
        else:
            return name

class RestaurantLocationModelForm(ModelForm):
    # category =  forms.CharField(required=False, validators=[validate_category])
    class Meta:
        model = RestaurantLocation
        fields = ['name', 'location', 'category']
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Hello':
            raise forms.ValidationError("Not a valid name")
        return name