from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .validators import validate_image_size, validate_image_extension

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(
        upload_to='profile_pics/', 
        blank=True, 
        null=True,
        validators=[validate_image_size, validate_image_extension]
    )
    full_name = models.CharField(max_length=200, blank=True)
    father_name = models.CharField(max_length=200, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
    
    @property
    def get_full_name(self):
        return self.full_name if self.full_name else self.user.username
    
    @property
    def profile_completion_percentage(self):
        completion = 0
        
        personal_fields = ['full_name', 'father_name', 'date_of_birth', 'phone', 'address', 'profile_picture']
        personal_filled = sum([1 for field in personal_fields if getattr(self, field)])
        if personal_filled >= 4:
            completion += 20
        
        if self.education_set.exists():
            completion += 20
        
        if self.skill_set.exists():
            completion += 20
        
        if self.experience_set.exists():
            completion += 20
        
        if self.project_set.exists():
            completion += 20
        
        return completion


class Education(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='education_set')
    university_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
    
    def __str__(self):
        return f"{self.degree} at {self.university_name}"


class Skill(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skill_set')
    skill_name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='intermediate')
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return f"{self.skill_name} ({self.level})"


class Experience(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='experience_set')
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
    
    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


class Project(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='project_set')
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    skills_used = models.CharField(max_length=300, help_text="Comma-separated skills")
    live_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return self.project_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
