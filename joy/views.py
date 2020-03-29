from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Events, Gallery, News, Careers, Partners
from django.core.mail import send_mail,BadHeaderError
from django.conf import settings
from.forms import ContactForm
from django.contrib import messages


def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            msg_mail = str(message) + " " + str(from_email)
            try:
                send_mail(subject, msg_mail , from_email, ['kimkidati@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    events = Events.objects.all()[:3]
    context = {
    'events':events,
    'form':form,
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

def about(request):
    return render(request, 'about.html')

def news(request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request, 'news.html', context)


def tenders(request):
    return render(request, 'tenders.html')

def partners(request):
    partners = Partners.objects.all()
    context = {
        'partners':partners
    }
    return render(request, 'partners.html', context)


def careers(request):
    careers = Careers.objects.all()
    context = {
        'careers':careers
    }
    return render(request, 'careers.html', context)


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            msg_mail = str(message) + " " + str(from_email)
            try:
                send_mail(subject, msg_mail , from_email, ['kimkidati@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.add_message(request, messages.SUCCESS, 'Email sent successfully.')
    return render(request, "contact.html", {'form': form,})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
    
def kiambu(request):
    return render(request, 'kiambu.html')
