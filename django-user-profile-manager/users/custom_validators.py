from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_username_unique(username):
    if User.objects.filter(username=username).exists():
        raise ValidationError('Username already taken')

def validate_email_unique(email):
    if User.objects.filter(email=email).exists():
        raise ValidationError('Email already registered')

def validate_profile_picture_size(image):
    max_size_mb = 5
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f'Image file too large. Maximum size is {max_size_mb}MB')

def validate_phone_format(phone):
    import re
    pattern = r'^\+?1?\d{9,15}$'
    if phone and not re.match(pattern, phone):
        raise ValidationError('Enter a valid phone number')

def validate_bio_length(bio):
    if bio and len(bio) < 10:
        raise ValidationError('Bio must be at least 10 characters long')
    if bio and len(bio) > 500:
        raise ValidationError('Bio must not exceed 500 characters')
