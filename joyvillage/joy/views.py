from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Events, Gallery, News, Careers
from django.core.mail import send_mail,BadHeaderError
from django.conf import settings
from.forms import ContactForm

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
    return render(request, 'partners.html')


def careers(request):
    careers = Careers.objects.all()
    context = {
        'careers':careers
    }
    return render(request, 'careers.html', context)


# def contact(request):
#     if request.method == "POST":
#         sender = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#
#         sender_list = [sender]
#         send_mail(
#             subject,
#             message,
#             sender,
#             ['kimkidati@gmail.com'])
#         return HttpResponse('Mail sended')
#
#     return render(request, 'contact.html')
#
# def success(request):
#     return HttpResponse('Success! Thank you for your message.')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']

            recipient = ['kimkidati@gmail.com']

            send_mail(
                name,
                message,
                sender,
                recipient,
            )
            form.save()
            print('Message sent succesfully')
            return redirect('contact')
        else:
            print('Message not sent')
        return render(request, 'contact.html', {'form':form,'name':name})
    # else:
    #     form = ContactForm(request.POST)
    # context = {
    #     'form':form,
    #     'name':name,
    #     'message':message,
    #     'sender':sender
    # }
    # return render(request, 'contact.html', context)
