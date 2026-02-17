"""
App configuration for the Notes application.
"""

from django.apps import AppConfig


class NotesConfig(AppConfig):
    """Configuration for the Notes app."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notes'
    verbose_name = 'Notes Management'
