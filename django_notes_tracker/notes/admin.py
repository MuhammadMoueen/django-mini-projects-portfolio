"""
Admin configuration for the Notes application.

This module registers the Note model with the Django admin site.
"""

from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """
    Admin interface for the Note model.
    
    Customizes how notes are displayed and managed in the Django admin panel.
    """
    
    # Fields to display in the list view
    list_display = ('title', 'created_at', 'content_preview')
    
    # Fields to search
    search_fields = ('title', 'content')
    
    # Filters in the sidebar
    list_filter = ('created_at',)
    
    # Read-only fields (created_at is auto-generated)
    readonly_fields = ('created_at',)
    
    # Ordering in the admin list view
    ordering = ('-created_at',)
    
    # Number of items per page
    list_per_page = 20
    
    def content_preview(self, obj):
        """
        Display a preview of the note content in the admin list view.
        
        Args:
            obj (Note): The Note instance
            
        Returns:
            str: First 50 characters of content
        """
        return obj.get_short_content(50)
    
    content_preview.short_description = 'Content Preview'
