from django.contrib import admin
from .models import UserProfile, Education, Skill, Experience, Project

admin.site.register(UserProfile)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)
