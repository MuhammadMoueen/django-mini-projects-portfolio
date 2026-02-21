# Django User Profile Manager

A professional Django application for comprehensive user profile management with dark neumorphic UI design.

## Features

### 🎨 Modern UI/UX
✅ Dark Neumorphic Design Theme
✅ Soft Shadows & Smooth Transitions
✅ Gradient Buttons & Animated Elements
✅ Fully Responsive Layout
✅ Profile Completion Progress Bar
✅ Consistent Design Across All Pages
✅ Profile Dropdown Menu with Avatar
✅ Image Crop Tool Before Upload

### 🔐 Authentication
✅ User Registration & Login
✅ Session Management
✅ Password Change
✅ Protected Routes

### 👤 Personal Information
✅ Profile Picture Upload with Image Cropping
✅ Full Name & Father Name
✅ Date of Birth
✅ Phone Number
✅ Complete Address

### 🎓 Education Management
✅ Add Multiple Education Entries
✅ University Name & Degree
✅ CGPA/Grade Tracking
✅ Start & End Dates
✅ Detailed Descriptions

### 🏆 Skills & Certifications
✅ Add Multiple Skills
✅ Proficiency Level Selector (Beginner to Expert)
✅ Certificate File Upload
✅ Certificate Link Support
✅ Visual Level Badges

### 💼 Work Experience
✅ Add Multiple Job Positions
✅ Company & Job Title
✅ Start/End Dates
✅ Current Position Indicator
✅ Role Descriptions

### 📁 Portfolio & Projects
✅ Add Multiple Projects
✅ Project Descriptions
✅ Skills Used Tags
✅ Live Demo Links
✅ GitHub Repository Links

### 📊 Profile Completion System
✅ Auto-calculated Completion Percentage
✅ 5 Section Tracking (20% each)
✅ Visual Progress Bar
✅ Section Status Indicators

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

```
django-user-profile-manager/
├── users/                          # Main application
│   ├── models.py                   # UserProfile, Education, Skill, Experience, Project
│   ├── views.py                    # All CRUD views
│   ├── forms.py                    # All forms for each section
│   ├── urls.py                     # URL routing
│   ├── admin.py                    # Admin panel configuration
│   ├── validators.py               # Image upload validators
│   ├── templates/users/            # All templates
│   │   ├── dashboard.html          # Main hub with section cards
│   │   ├── personal_info.html      # Personal information form
│   │   ├── education_list.html     # List all education entries
│   │   ├── education_form.html     # Add/Edit education
│   │   ├── skills_list.html        # List all skills
│   │   ├── skill_form.html         # Add/Edit skills
│   │   ├── experience_list.html    # List all experiences
│   │   ├── experience_form.html    # Add/Edit experience
│   │   ├── projects_list.html      # List all projects
│   │   ├── project_form.html       # Add/Edit projects
│   │   └── confirm_delete.html     # Delete confirmation
│   └── static/
│       └── css/
│           └── style.css           # Neumorphic theme styles
├── profile_manager/                # Project settings
├── media/                          # Uploaded files
│   ├── profile_pics/               # Profile pictures
│   └── certificates/               # Skill certificates
└── db.sqlite3                      # Database

```

## Technology Stack

- **Backend**: Django 5.2.11
- **Frontend**: Bootstrap 5.3 + Custom Neumorphic CSS
- **Image Crop**: Cropper.js 1.6.1
- **Database**: SQLite3
- **Image Processing**: Pillow 12.1.1
- **Icons**: Bootstrap Icons
- **Authentication**: Django Built-in Auth System

## All Pages & Routes

### Authentication
- `/register/` - User registration with form validation
- `/login/` - User login
- `/logout/` - Logout and session cleanup

### Dashboard
- `/dashboard/` - Main hub with profile completion and section cards

### Personal Information
- `/personal-info/` - Edit personal details (name, DOB, phone, address)

### Education
- `/education/` - List all education entries
- `/education/add/` - Add new education
- `/education/<id>/edit/` - Edit education entry
- `/education/<id>/delete/` - Delete education entry

### Skills & Certifications
- `/skills/` - List all skills with level badges
- `/skills/add/` - Add new skill
- `/skills/<id>/edit/` - Edit skill
- `/skills/<id>/delete/` - Delete skill

### Experience
- `/experience/` - List all work experiences
- `/experience/add/` - Add new experience
- `/experience/<id>/edit/` - Edit experience
- `/experience/<id>/delete/` - Delete experience

### Projects
- `/projects/` - List all portfolio projects
- `/projects/add/` - Add new project
- `/projects/<id>/edit/` - Edit project
- `/projects/<id>/delete/` - Delete project

### Other
- `/profile/` - View own profile
- `/password/change/` - Change password

## Usage Guide

### First Time Setup
1. Register a new account at `/register/`
2. Login with your credentials
3. You'll be redirected to the Dashboard

### Dashboard Overview
The dashboard displays your profile picture, name, completion percentage, and 5 section cards.

### Completing Your Profile
Each section is worth 20% completion:
1. **Personal Information**: name, DOB, phone, address
2. **Education**: Add at least one entry
3. **Skills**: Add at least one skill
4. **Experience**: Add at least one position
5. **Projects**: Add at least one project

## Design Features

### Neumorphic UI
- Soft shadows create depth
- Dark navy background (#2E3A59)
- Coral gradient buttons (#FF6B8A)
- Smooth transitions

### Responsive
- Desktop: Full layout
- Tablet: Stacked columns  
- Mobile: Compact view

## License
MIT License - Portfolio Project 2026
