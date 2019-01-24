from django.conf.urls import url, include
from django.contrib import admin
from restaurants.views import (
    RetaurantListView, 
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView
)

urlpatterns = [
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    # url(r'^(?P<slug>[\w-]+)/update/$', RestaurantUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/details/$', RestaurantDetailView.as_view(), name='details'),
    url(r'^$', RetaurantListView.as_view(), name='list')
]