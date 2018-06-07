from django.contrib import admin
from django.conf.urls import include, url


from .models import RestaurantLocation, UserGroup, CourseName, CourseGroup


class BasicAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(BasicAdmin, self).get_urls()
        urlpatterns = [
            '',
            (r'^restautants/add/$', self.re)
        ]
        return urlpatterns + urls

admin.site.register(RestaurantLocation)
admin.site.register(UserGroup)
admin.site.register(CourseName)
admin.site.register(CourseGroup)