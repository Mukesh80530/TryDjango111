from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')), 
]
