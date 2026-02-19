from django.core.exceptions import ValidationError
import os

def validate_image_size(image):
    file_size = image.size
    limit_mb = 5
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(f"Max file size is {limit_mb}MB")

def validate_image_extension(image):
    ext = os.path.splitext(image.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError(f"Unsupported file extension. Allowed: {', '.join(valid_extensions)}")

def validate_phone_number(phone):
    if phone and not phone.replace('+', '').replace('-', '').replace(' ', '').isdigit():
        raise ValidationError("Enter a valid phone number")
