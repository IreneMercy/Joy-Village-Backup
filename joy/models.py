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
        verbose_name_plural = "UpcomingEvents"

class PastEvents(models.Model):
    date = models.CharField(max_length=10)
    venue = models.CharField(max_length=100)
    time = models.CharField(max_length=30)
    image = models.ImageField()
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pub_date']
        verbose_name_plural = "PastEvents"

class Gallery(models.Model):
    imagefield = models.ImageField(upload_to="media")
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pub_date']
        verbose_name_plural = "Gallery"

class News(models.Model):
    newsimage = models.ImageField(upload_to="media", blank=True)
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['pub_date']
        verbose_name_plural = "News"

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
        verbose_name_plural = "Careers"


class Partners(models.Model):
    partnerimage = models.ImageField(upload_to="media")
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Partners"

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    timespan = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.content

class About(models.Model):
    introtext = models.TextField(max_length=500)
    missionheading = models.CharField(max_length=30)
    missiontext = models.TextField(max_length=500)
    visionheading = models.TextField(max_length=30)
    visiontext = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media', blank=True)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.introtext

class Nairobi(models.Model):
    ProgramOnset = models.CharField(max_length=10)
    ProgramLocation = models.CharField(max_length=100)
    ProgramTitle = models.CharField(max_length=30)
    image = models.ImageField()
    ProgramDescription = models.TextField(max_length=500)
    donate = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Nairobi"

    def __str__(self):
        return self.ProgramTitle

class Kiambu(models.Model):
    ProgramOnset = models.CharField(max_length=10)
    ProgramLocation = models.CharField(max_length=100)
    ProgramTitle = models.CharField(max_length=30)
    ProgramImage = models.ImageField()
    ProgramDescription = models.TextField(max_length=500)
    donate = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Kiambu"

    def __str__(self):
        return self.ProgramTitle

class Muranga(models.Model):
    ProgramOnset = models.CharField(max_length=10)
    ProgramLocation = models.CharField(max_length=100)
    ProgramTitle = models.CharField(max_length=30)
    ProgramImage = models.ImageField()
    ProgramDescription = models.TextField(max_length=500)
    donate = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Muranga"

    def __str__(self):
        return self.ProgramTitle

class Nyeri(models.Model):
    ProgramOnset = models.CharField(max_length=10)
    ProgramLocation = models.CharField(max_length=100)
    ProgramTitle = models.CharField(max_length=30)
    ProgramImage = models.ImageField()
    ProgramDescription = models.TextField(max_length=500)
    donate = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Nyeri"
    def __str__(self):
        return self.ProgramTitle

class Nakuru(models.Model):
    ProgramOnset = models.CharField(max_length=10)
    ProgramLocation = models.CharField(max_length=100)
    ProgramTitle = models.CharField(max_length=30)
    ProgramImage = models.ImageField()
    ProgramDescription = models.TextField(max_length=500)
    donate = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Nakuru"
    def __str__(self):
        return self.ProgramTitle

class YouthGroup(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'YouthGroups'

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.TextField(max_length=100)
    answer = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = 'FAQs'
    def __str__(self):
        return self.question
