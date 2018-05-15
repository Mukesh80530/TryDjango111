from django.db import models

class RestaurantLocation(models.Model):
	name = models.CharField(max_length=120)
	location = models.CharField(max_length=120, null=True, blank=True)

	def __unicode__(self):
		return name
