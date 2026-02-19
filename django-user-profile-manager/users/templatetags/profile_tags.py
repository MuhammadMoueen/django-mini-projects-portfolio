from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.filter
def profile_completion(user):
    profile = user.profile
    fields = ['full_name', 'bio', 'phone', 'location', 'profile_picture']
    filled = sum([1 for field in fields if getattr(profile, field)])
    return int((filled / len(fields)) * 100)

@register.filter
def user_initials(user):
    if user.profile.full_name:
        names = user.profile.full_name.split()
        return ''.join([n[0].upper() for n in names[:2]])
    return user.username[0].upper()

@register.simple_tag
def total_profiles():
    return User.objects.count()

@register.simple_tag
def active_users():
    return User.objects.filter(is_active=True).count()
