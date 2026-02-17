from django.db import models


class Note(models.Model):

    title = models.CharField(
        max_length=200,
        help_text="Enter the note title"
    )
    
    content = models.TextField(
        help_text="Enter the note content"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the note was created"
    )
    
    class Meta:
        
        ordering = ['-created_at']  # Most recent notes first
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
    
    def __str__(self):
        return self.title
    

