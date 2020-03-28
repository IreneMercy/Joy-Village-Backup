from __future__ import unicode_literals
from django.db import models
from django.db import models

class Events(models.Model):
    date = models.CharField(max_length=10)
    venue = models.CharField(max_length=100)
    time = models.CharField(max_length=30)
    image = models.ImageField()
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=155)
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
class News(models.Model):
    newsimage = models.ImageField(upload_to="media")
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['pub_date']

class Careers(models.Model):
    position = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    requirements = models.CharField(max_length=255)
    instruction = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.position

    class  Meta:
        ordering = ['pub_date']


class Partners(models.Model):
    partnerimage = models.ImageField(upload_to="media")
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
