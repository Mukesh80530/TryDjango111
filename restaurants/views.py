from django.shortcuts import render
import random
from django.views import View
from .models import RestaurantLocation
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.db.models import Q

class homeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(homeView, self).get_context_data(*args, **kwargs)
        num = None
        some_list = [
            random.randint(1, 100000), 
            random.randint(1, 100000), 
            random.randint(1, 10000)
        ]
        condition_bool_item = True
        if condition_bool_item:
            num = random.randint(0,100000)
        context = {
            'num':num,
            'some_list':some_list
        }
        return context

# class AboutView(TemplateView):
#     template_name = 'about.html'

# class ContactView(TemplateView):
#     template_name = 'contact.html'

def Retaurant_ListView(request):
    query_set = RestaurantLocation.objects.all()
    template_name = 'restaurants_list.html'
    context = {
        'object_list':query_set
    }
    return render(request, template_name, context)

class SearchRestaurantListView(ListView):
    template_name = 'restaurants_list.html'
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) | 
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.none()
        return queryset 
