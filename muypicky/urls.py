from django.conf.urls import url
from django.contrib import admin
from restaurants.views import home, ContactClassView, AboutTemplateView # contact, about

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    # url(r'^about/$', about),
    url(r'^about/$', AboutTemplateView.as_view()),
    # url(r'^contact/$', contact),
    url(r'^contact/$', ContactClassView.as_view()),
]
