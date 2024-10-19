from django.contrib import admin
from .models import Event, Interest, EventUser

# Register your models here.
admin.site.register(Event)
admin.site.register(Interest)
# admin.site.register(Events_sub)
admin.site.register(EventUser)