from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('events', views.events, name='events'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('careers', views.careers, name='careers'),
    path('tenders', views.tenders, name='tenders'),
    path('partners', views.partners, name='partners'),
    path('success/', views.successView, name='success'),
    path('kiambu', views.kiambu, name='kiambu')





]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
