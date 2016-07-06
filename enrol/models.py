from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Enrolment(models.Model):
    name = models.CharField(max_length=250)  # name of the course
    student = models.ForeignKey(User, related_name='Student')
    code = models.CharField(max_length=10)  # course code
    duration = models.IntegerField(default=0)  # course duration
    batch = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
