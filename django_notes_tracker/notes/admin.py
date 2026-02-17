from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'content_preview')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 20
    
    def content_preview(self, obj):
        return obj.get_short_content(50)
    
    content_preview.short_description = 'Content Preview'
