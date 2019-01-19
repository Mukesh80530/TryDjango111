from django.conf.urls import url, include
from django.contrib import admin
from restaurants.views import (
    Retaurant_ListView, 
    SearchRestaurantListView,
    RestaurantDetailView,
    restaurant_createview,
)
from django.views.generic import TemplateView

urlpatterns = [
    # class based views
    url(r'^restaurants/$', Retaurant_ListView, name='restaurants_list'),
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    url(r'^search/(?P<slug>\w+)/$', SearchRestaurantListView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # function based views
    url(r'^restaurants/create/$', restaurant_createview, name='restaurant_create')
]