# Django User Profile Manager

A professional Django application for managing user profiles with authentication, image uploads, and profile customization.

## Features

✅ User Registration & Authentication
✅ Login & Logout with Session Management
✅ Protected Dashboard
✅ Profile Creation & Editing
✅ Profile Picture Upload with Validation
✅ Bio & Contact Information Fields
✅ Password Change Functionality
✅ Modern Dark Theme UI
✅ Responsive Bootstrap Design
✅ Security: Users can only edit their own profiles
✅ Profile Completion Tracking
✅ Custom Template Tags
✅ Image Upload Validators
✅ Management Commands for Demo Data

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Create superuser (optional):
```bash
python manage.py createsuperuser
```

4. Run development server:
```bash
python manage.py runserver
```

5. Visit http://127.0.0.1:8000

## Project Structure

- `users/` - Main application
- `profile_manager/` - Project settings
- `media/` - Uploaded profile pictures
- `static/` - CSS and JavaScript files

## Profile Fields

- Profile Picture (optional)
- Full Name
- Email (required)
- Bio
- Phone (optional)
- Location (optional)

## Technology Stack

- Django 5.0.14
- Bootstrap 5
- SQLite Database
- Pillow for Image Processing

## Pages

- `/register/` - User registration
- `/login/` - User login
- `/dashboard/` - User dashboard
- `/profile/` - View profile
- `/profile/edit/` - Edit profile
- `/password/change/` - Change password
- `/logout/` - Logout
