from django.contrib import admin
from .models import UserProfile, Education, Skill, Experience, Project

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'phone', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'full_name', 'phone']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['profile', 'degree', 'university_name', 'cgpa', 'start_date']
    list_filter = ['created_at']
    search_fields = ['university_name', 'degree']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['profile', 'skill_name', 'level', 'created_at']
    list_filter = ['level', 'created_at']
    search_fields = ['skill_name']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['profile', 'job_title', 'company_name', 'start_date', 'is_current']
    list_filter = ['is_current', 'created_at']
    search_fields = ['job_title', 'company_name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['profile', 'project_name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['project_name', 'skills_used']
