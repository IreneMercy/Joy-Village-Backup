from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('events', views.upcomingevents, name='upcoming'),
    path('pastevent', views.pastevents, name='past'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('careers', views.careers, name='careers'),
    path('tenders', views.tenders, name='tenders'),
    path('partners', views.partners, name='partners'),
    path('about', views.about, name='about'),
    path('kiambu', views.kiambu, name='kiambu'),
    path('nairobi', views.nairobi, name='nairobi'),
    path('muranga', views.muranga, name='muranga'),
    path('nyeri', views.nyeri, name='nyeri'),
    path('nakuru', views.nakuru, name='nakuru'),
    path('donate/<int:pk>/', views.donate, name='donate'),
    path('complete', views.paymentcomplete, name='complete')







]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
