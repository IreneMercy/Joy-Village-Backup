from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Events, Gallery
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    events = Events.objects.all()[:3]
    context = {
    'events':events,
    }
    return render(request,'home.html', context)

def events(request):
    events = Events.objects.all()
    context = {
    'events':events,
    }
    return render(request, 'events.html', context)

def gallery(request):
    gallery = Gallery.objects.all()
    context = {
    'gallery':gallery,
    }
    return render(request, 'gallery.html', context)

def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        subject = request.POST['subject']
        send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['irenemercy700@gmail.com'],
        fail_silently=False)
    return render(request, 'contact.html')
