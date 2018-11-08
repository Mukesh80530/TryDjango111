from django.conf.urls import url, include
from django.contrib import admin
from restaurants.views import (
    Retaurant_ListView, 
    SearchRestaurantListView,
    RestaurantDetailView
     #AboutView, 
     #ContactView
)
from django.views.generic import TemplateView

urlpatterns = [
    # class based views
    url(r'^restaurants/$', Retaurant_ListView, name='restaurants_list'),
    # url(r'^restaurants/(?P<pk>\w+)/$', RestaurantDetailView.as_view()),
    url(r'^restaurants/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view()),
    url(r'^search/(?P<slug>\w+)/$', SearchRestaurantListView.as_view()),

    # function based views
    # url(r'^about/$', AboutView.as_view(), name='about'),
    # url(r'^contact/$', ContactView.as_view(), name='contact'),

    # class based views
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # url(r'^add/$', views.CreateRestaurant, name='create_restaurant'),
]
