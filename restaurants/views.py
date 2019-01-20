from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from .models import RestaurantLocation
from .forms import RestaurantLocationDjangoForm, RestaurantLocationModelForm

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

@login_required()
def restaurant_createview(request):
    # django form method
    # form = RestaurantLocationDjangoForm(request.POST or None)

    # django form method
    form = RestaurantLocationModelForm(request.POST or None)
    errors = None
    if form.is_valid():
        # django form method
        # obj =  RestaurantLocation.objects.create(
        #     name =  form.cleaned_data.get('name'),
        #     location = form.cleaned_data.get('location'),
        #     category = form.cleaned_data.get('category')
        # )
        
        # django model form
        if request.user.is_authenticated():
            instance =  form.save(commit=False)
            instance.ower = request.user
            form.save() 
            return HttpResponseRedirect('/restaurants/')
        else:
            return HttpResponseRedirect('/login/')
    if form.errors:
        errors = form.errors
    template_name = 'form.html'
    context = {'form': form,'errors':errors}
    return render(request, template_name, context)

class restaurant_createview(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationModelForm
    template_name = 'form.html'
    login_url = '/accounts/login/' # or orther login page
    # success_url = "/restaurants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.ower =  self.request.user
        return super(restaurant_createview, self).form_valid(form)