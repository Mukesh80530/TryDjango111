from django.conf.urls import url, include
from django.contrib import admin
from restaurants.views import (
    Retaurant_ListView, 
    SearchRestaurantListView,
    RestaurantDetailView,
    # restaurant_createview,
    restaurant_createview,
)

urlpatterns = [
    # class based views
    url(r'^$', Retaurant_ListView, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='details'),
    url(r'^create/$', restaurant_createview.as_view(), name='create'),
    url(r'^search/(?P<slug>\w+)/$', SearchRestaurantListView.as_view(), name='search'),

    # function based views
    # url(r'^create/$', restaurant_createview, name='restaurant_create')
]