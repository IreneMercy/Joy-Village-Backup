from __future__ import unicode_literals
from django.contrib import admin
from .models import Events, Gallery, News, Careers

admin.site.register(Events),
admin.site.register(Gallery),
admin.site.register(News),
admin.site.register(Careers),
