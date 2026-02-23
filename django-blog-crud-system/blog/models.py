from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    """
    Blog post model with full CRUD functionality.
    
    Attributes:
        title: Post title (max 200 characters)
        content: Post content (unlimited text)
        author: Foreign key to User model
        created_at: Timestamp when post was created
        updated_at: Timestamp when post was last modified
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    
    @property
    def is_recently_updated(self):
        return self.updated_at > self.created_at

class UserProfile(models.Model):
    """
    User profile model with additional user information.
    
    Attributes:
        user: One-to-one relationship with User model
        bio: User biography (max 500 characters)
        profile_pic: User profile picture (uploaded to profile_pics/)
        created_at: Timestamp when profile was created
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    @property
    def total_posts(self):
        return self.user.posts.count()
    
    @property
    def profile_picture(self):
        if self.profile_pic:
            return self.profile_pic.url
        return None
    
    def get_full_name(self):
        """
        Returns the user's full name if available, otherwise returns username.
        """
        full_name = f"{self.user.first_name} {self.user.last_name}".strip()
        return full_name if full_name else self.user.username
    
    def get_display_name(self):
        """
        Returns formatted display name with 'Written by' prefix.
        """
        return f"Written by {self.get_full_name()}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
