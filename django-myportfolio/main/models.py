from django.db import models
from django.core.validators import FileExtensionValidator

class CV(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(
        blank=True,
        help_text='Brief description shown above the download button'
    )
    file = models.FileField(
        upload_to='cvs/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'CVs'
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.is_active:
            CV.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super(CV, self).save(*args, **kwargs)

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('fullstack', 'Full Stack'),
        ('django', 'Django'),
        ('backend', 'Backend'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    pdf_file = models.FileField(
        upload_to='projects/pdfs/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        help_text='Optional PDF documentation for this project'
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='fullstack')
    technologies = models.CharField(
        max_length=500,
        help_text='Comma-separated list of technologies'
    )
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-featured', 'order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.email}"
