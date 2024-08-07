from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Client

User = get_user_model()

@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        # Create a Client instance when a new User is created
        Client.objects.create(user=instance, name=instance.username, email=instance.email)
