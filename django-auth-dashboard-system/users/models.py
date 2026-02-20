from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=500, blank=True, null=True)
    education = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
