from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def check_username_exists(username):
    return User.objects.filter(username=username).exists()

def check_email_exists(email):
    return User.objects.filter(email=email).exists()

def get_user_profile_completion(user):
    profile = user.profile
    fields = ['full_name', 'bio', 'phone', 'location', 'profile_picture']
    filled = sum([1 for field in fields if getattr(profile, field)])
    return int((filled / len(fields)) * 100)

def format_profile_stats(profile):
    return {
        'completion': get_user_profile_completion(profile.user),
        'has_image': bool(profile.profile_picture),
        'has_bio': bool(profile.bio),
        'has_contact': bool(profile.phone),
    }
