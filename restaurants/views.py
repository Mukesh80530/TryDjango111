from django.shortcuts import render, get_object_or_404
import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from django.db.models import Q

from .models import RestaurantLocation
from .forms import RestaurantCreateForm

def Retaurant_ListView(request):
    query_set = RestaurantLocation.objects.all()
    template_name = 'restaurants_list.html'
    context = {
        'object_list':query_set
    }
    return render(request, template_name, context)

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()
    template_name = 'restaurantlocation_detail.html'
    # def get_context_data(self, *args, **kwargs):
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     return context
    
    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj =  get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj

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
            queryset = RestaurantLocation.objects.all()
        return queryset 

def restaurant_createview(request):
    import pdb; pdb.set_trace()
    template_name = 'form.html'
    context = {}
    return render(request, template_name, context)