from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Lawyer, Client, Appointment
admin.site.register(Lawyer)
admin.site.register(Client)
admin.site.register(Appointment)
