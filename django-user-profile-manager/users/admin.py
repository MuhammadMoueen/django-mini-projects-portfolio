from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'phone', 'location', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'full_name', 'phone', 'location']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'full_name', 'profile_picture')
        }),
        ('Contact Details', {
            'fields': ('phone', 'location')
        }),
        ('Bio', {
            'fields': ('bio',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
