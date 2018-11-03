from django.conf.urls import url, include
from django.contrib import admin
from restaurants.views import homeView, Retaurant_ListView, SearchRestaurantListView #AboutView, ContactView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', homeView.as_view(), name='home'),

    # function based views
    # url(r'^about/$', AboutView.as_view(), name='about'),
    # url(r'^contact/$', ContactView.as_view(), name='contact'),

    # class based views
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^search/(?P<slug>\w+)/$', SearchRestaurantListView.as_view()),

    # url(r'^add/$', views.CreateRestaurant, name='create_restaurant'),
    url(r'^list/$', Retaurant_ListView, name='restaurants_list'),
]
