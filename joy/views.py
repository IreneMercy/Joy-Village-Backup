from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Events, Gallery, News, Careers, Partners, Testimonials, About, Nairobi, Kiambu, Muranga, Nyeri, Nakuru, PastEvents
from django.core.mail import send_mail,BadHeaderError
from django.conf import settings
from.forms import ContactForm, CommentForm
from django.contrib import messages
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
import json


def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            reply_to=[from_email]
            msg_mail = str(message) + " " + str(from_email)
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    ['kimkidati@gmail.com'],
                    reply_to,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    events = Events.objects.all()[:3]
    comments = Testimonials.objects.all()
    context = {
    'events':events,
    'form':form,
    'comments':comments,
    }
    messages.info(request, messages.SUCCESS, 'Email sent successfully.')
    return render(request,'home.html', context)

def upcomingevents(request):
    events = Events.objects.all()
    context = {
    'events':events,
    }
    return render(request, 'events.html', context)


def pastevents(request):
    events = PastEvents.objects.all()
    context = {
    'events':events,
    }
    return render(request, 'pastevents.html', context)

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
            reply_to=[from_email]
            msg_mail = str(message) + " " + str(from_email)
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    ['kimkidati@gmail.com'],
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    messages.info(request, messages.SUCCESS, 'Email sent successfully.')
    return render(request, "contact.html", {'form': form,})




def about(request):
    about = About.objects.all()
    context = {
        'about':about
    }
    return render(request, 'about.html', context)



def kiambu(request):
    programs = Kiambu.objects.all()
    context = {
    'programs':programs
    }
    return render(request, 'kiambu.html', context)

def nairobi(request):
    programs = Nairobi.objects.all()
    context = {
    'programs':programs
    }
    return render(request, 'nairobi.html', context)


def muranga(request):
    programs = Muranga.objects.all()
    context = {
    'programs':programs
    }
    return render(request, 'muranga.html', context)

def nyeri(request):
    programs = Nyeri.objects.all()
    context = {
    'programs':programs
    }
    return render(request, 'nyeri.html', context)

def nakuru(request):
    programs = Nakuru.objects.all()
    context = {
    'programs':programs
    }
    return render(request, 'nakuru.html', context)


def donate(request, pk):
    program = Kiambu.objects.get(id=pk)
    context = {
        'program':program
    }
    return render(request, 'donate.html', context)

def paymentcomplete(request):
    body=json.loads(request.body)
    print('Body:', body)
    return JsonResponse('Payment completed!', safe=False)
    
def faqs(request):
    return render(request, 'faq.html')
