from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('lawyer', 'Lawyer'),
        ('client', 'Client'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)


from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth.models import User
class Lawyer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name
# class Appointment(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE,default='')
#     lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE,default='')
#     date = models.DateTimeField(default=timezone.now)
#     reason = models.TextField()
#     def __str__(self):
#         return f"Appointment with {self.lawyer} on {self.date}"


from django.db import models
from django.utils import timezone

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default='')
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, default='')
    date = models.DateTimeField(default=timezone.now)
    reason = models.TextField()
    contact_number = models.CharField(max_length=15, default='')  # Add default value here
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return f"Appointment with {self.lawyer} on {self.date}"
