from django.shortcuts import render
import random
from django.views import View
from .models import RestaurantLocation
from django.views.generic import TemplateView
from django.http import HttpResponse


def home(request):
	num =  random.randint(0,100000,)
	some_list = [random.randint(1,100000), random.randint(1,100000), random.randint(1,10000)]
	var = 'this is simples string'
	return render(request, 'home.html', {'html_var':var,'num':num,'var': True, 'some_list':some_list})


# def about(request):
# 	return render(request, 'about.html', {})

# class AboutTemplateView(TemplateView):
# 	template_name = 'about.html'

# def contact(request):
# 	return render(request, 'contact.html', {})

class ContactClassView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'contact.html', context)

    # def post(self, request,*args, **kwargs):
    # 	context = {}
    # 	return render(request, 'contact.html', context)

    # def put(self, request,*args, **kwargs):
    # 	context = {}
    # 	return render(request, 'contact.html', context)


def Retaurant_ListView(request):
    queryset =  RestaurantLocation.objects.all()
    context = {'object_list':queryset}
    return render(request, 'restaurants_list.html', context)