from django.contrib import admin
from django.utils.html import format_html
from .models import CV, Project, ContactMessage


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'file_info', 'uploaded_at']
    list_filter = ['is_active', 'uploaded_at']
    search_fields = ['title', 'description']
    readonly_fields = ['uploaded_at', 'updated_at']
    fieldsets = (
        ('CV Information', {
            'fields': ('title', 'description', 'file', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('uploaded_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def file_info(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank">View PDF</a>', obj.file.url)
        return "No file"
    file_info.short_description = 'File'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order', 'has_image', 'has_pdf', 'created_at']
    list_filter = ['category', 'featured', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['featured', 'order']
    readonly_fields = ['created_at', 'updated_at', 'preview_image']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'category')
        }),
        ('Media', {
            'fields': ('image', 'preview_image', 'pdf_file')
        }),
        ('Details', {
            'fields': ('technologies', 'live_url', 'github_url')
        }),
        ('Settings', {
            'fields': ('featured', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_image(self, obj):
        if obj.image:
            return format_html('<span style="color: green;">✓</span>')
        return format_html('<span style="color: red;">✗</span>')
    has_image.short_description = 'Image'
    
    def has_pdf(self, obj):
        if obj.pdf_file:
            return format_html('<a href="{}" target="_blank" style="color: green;">✓ View</a>', obj.pdf_file.url)
        return format_html('<span style="color: gray;">—</span>')
    has_pdf.short_description = 'PDF'
    
    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 300px; max-height: 300px; border-radius: 8px;"/>', obj.image.url)
        return "No image uploaded"
    preview_image.short_description = 'Preview'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_read', 'created_at', 'preview_message']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at', 'full_message']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Message', {
            'fields': ('full_message',)
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )
    
    def preview_message(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    preview_message.short_description = 'Message Preview'
    
    def full_message(self, obj):
        return format_html('<div style="padding: 10px; background: #f5f5f5; border-radius: 5px;">{}</div>', obj.message)
    full_message.short_description = 'Full Message'


# Customize admin site headers
admin.site.site_header = "Muhammad Moueen Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"
