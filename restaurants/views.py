from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect

from .models import RestaurantLocation
from .forms import RestaurantLocationDjangoForm, RestaurantLocationModelForm

class RetaurantListView(LoginRequiredMixin, ListView):
    template_name = 'restaurants_list.html'
    def get_queryset(self):
        return RestaurantLocation.objects.filter(ower=self.request.user)
   
class RestaurantDetailView(LoginRequiredMixin, DetailView):
    template_name = 'restaurantlocation_detail.html'
    def get_queryset(self):
        return RestaurantLocation.objects.filter(ower=self.request.user)

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationModelForm
    template_name = 'form.html'
    login_url = '/accounts/login/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.ower =  self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationModelForm
    login_url = '/accounts/login/'
    template_name = 'restaurants/detail-update.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        name =  self.get_object().name
        context['title'] = f'Update Restaurant: {name}'
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(ower=self.request.user)
