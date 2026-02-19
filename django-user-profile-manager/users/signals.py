from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile
import os

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

@receiver(pre_delete, sender=UserProfile)
def delete_profile_picture(sender, instance, **kwargs):
    if instance.profile_picture:
        if os.path.isfile(instance.profile_picture.path):
            os.remove(instance.profile_picture.path)
