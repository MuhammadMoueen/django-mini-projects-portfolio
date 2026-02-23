from django.contrib import admin
from .models import CV, Project, ContactMessage

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'uploaded_at']
    list_filter = ['is_active', 'uploaded_at']
    search_fields = ['title']
    readonly_fields = ['uploaded_at', 'updated_at']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order', 'created_at']
    list_filter = ['category', 'featured', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['featured', 'order']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
