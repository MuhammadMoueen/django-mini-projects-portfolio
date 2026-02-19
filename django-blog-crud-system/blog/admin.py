from django.contrib import admin
from .models import Post, UserProfile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_posts')
    search_fields = ('user__username', 'bio')
