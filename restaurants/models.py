from django.db import models


class RestaurantLocation(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=False)
    category = models.CharField(max_length=120, null=True, blank=False)
    timestamp =  models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    @property
    def title(self):
        return self.name
