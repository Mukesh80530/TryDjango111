from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from restaurants.models import RestaurantLocation

class Item(models.Model):
    # associations
    user       = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(RestaurantLocation)
    # item stuff
    name       = models.CharField(max_length=120)
    contents   = models.TextField(help_text="Seprate each item by comma")
    excludes   = models.TextField(blank=True, null=True, help_text="Seprate each item by comma")
    public     = models.BooleanField(default=True)
    timestamp  = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menus:details', kwargs={'pk':self.pk})
    
    def get_contents(self):
        return self.contents.split(",")
    
    def get_excludes(self):
        return self.excludes.split(",")