from django.conf.urls import url
from django.contrib import admin
from restaurants.views import home, ContactClassView #AboutTemplateView  contact, about
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),

    # url(r'^about/$', about),
    # url(r'^about/$', AboutTemplateView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),

    # url(r'^contact/$', contact),
    url(r'^contact/$', ContactClassView.as_view()),
]
