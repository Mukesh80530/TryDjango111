from django.db import models
from django.contrib.auth.models import User, Group


class RestaurantLocation(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=False)
    category = models.CharField(max_length=120, null=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserGroup(models.Model):
    user_name = models.ForeignKey(User)
    group_name = models.ForeignKey(Group)


class CourseName(models.Model):
    course_name = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.course_name

class CourseGroup(models.Model):
    course_name = models.ForeignKey(CourseName)
    group_name = models.ForeignKey(Group)

    # def __str__(self):
    #     return self.course_name