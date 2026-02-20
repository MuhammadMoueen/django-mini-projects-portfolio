from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

admin.site.site_header = "Auth Dashboard Admin"
admin.site.site_title = "Auth Dashboard"
admin.site.index_title = "Welcome to Auth Dashboard Admin Panel"

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'skills', 'education')
    search_fields = ('user__username', 'skills', 'education')
    list_filter = ('date_of_birth',)
