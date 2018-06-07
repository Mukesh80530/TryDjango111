from django.conf.urls import url, include
from django.contrib import admin
from restaurants.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),

    # url(r'^about/$', about),
    # url(r'^about/$', AboutTemplateView.as_view()),
    url(r'^restaurants/', include('restaurants.urls')),
    # url(r'^about/$', TemplateView.as_view(template_name='about.html')),

    # url(r'^contact/$', contact),
    # url(r'^contact/$', ContactClassView.as_view()),

    # url(r'^restaurant_list/$', Retaurant_ListView, name='restaurant_list'),
]
