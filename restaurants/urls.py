from django.conf.urls import url, include
from django.contrib import admin
from restaurants.views import home, ContactClassView, Retaurant_ListView  # AboutTemplateView  contact, about
from django.views.generic import TemplateView
from restaurants import views

urlpatterns = [
    # url(r'^about/$', about),
    # url(r'^about/$', AboutTemplateView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),

    # url(r'^contact/$', contact),
    url(r'^contact/$', ContactClassView.as_view()),

    url(r'^add/$',views.CreateRestaurant, name='create_restaurant'),

    # url(r'^restaurant_list/$', Retaurant_ListView, name='restaurant_list'),
    url(r'^list/$', Retaurant_ListView, name='restaurant_list'),


]
