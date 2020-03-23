from __future__ import unicode_literals
from django.db import models
from django.db import models

class Events(models.Model):
    date = models.CharField(max_length=10)
    venue = models.CharField(max_length=100)
    time = models.CharField(max_length=30)
    image = models.ImageField()
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=155)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pub_date']


class Gallery(models.Model):
    imagefield = models.ImageField(upload_to="media")
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pub_date']
