# Muhammad Moueen - Professional Portfolio

A modern, professional Django-based portfolio website featuring dynamic project showcases, CV management, and client communication tools.

## ✨ Features

### Core Functionality
- **Dynamic Project Showcase**: Filter and display projects by category with featured highlights
- **CV Download System**: Upload CV/resume as PDF with description and one-click download
- **AJAX Contact Form**: Real-time form submission with email notifications
- **Admin Dashboard**: Comprehensive Django admin with image previews and file management
- **Project PDF Upload**: Attach documentation or additional resources to projects

### Design & UX
- **Responsive Design**: Mobile-first approach with seamless tablet and desktop experience
- **Dark Theme**: Modern dark mode with purple accent colors and gradient effects
- **Smooth Animations**: Fade-in effects, hover interactions, and glass morphism UI
- **Professional Typography**: Inter and JetBrains Mono font combinations
- **Optimized Performance**: CSS and JS cache-busting, lazy loading, and minimal dependencies

## 🚀 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django 5.2.7, Python 3.14 |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Database** | SQLite (Development) |
| **Icons** | Lucide Icons |
| **Fonts** | Google Fonts (Inter, JetBrains Mono) |
| **Image Processing** | Pillow 11.2.0 |
| **Static Files** | WhiteNoise 6.6.0 |
| **Email** | Django SMTP Backend |

## 📋 Prerequisites

- Python 3.8+ (Python 3.14 recommended)
- pip (Python package installer)
- Git
- Virtual environment tool

## 🛠️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/MuhammadMoueen/django-mini-projects-portfolio.git
cd django-mini-projects-portfolio/django-myportfolio
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```
Follow prompts to  set username, email, and password.

### 7. (Optional) Load Sample Data
```bash
python manage.py setup_portfolio
```
This creates demo projects and a test superuser (admin/admin123).

### 8. Run Development Server
```bash
python manage.py runserver
```

### 9. Access Application
- **Portfolio**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
django-myportfolio/
├── main/                          # Core application
│   ├── management/               # Custom management commands
│   │   └── commands/
│   │       └── setup_portfolio.py
│   ├── migrations/               # Database migrations
│   │   ├── 0001_initial.py
│   │   └── 0002_cv_description_project_pdf_file.py
│   ├── static/                   # Static assets
│   │   ├── css/
│   │   │   └── style.css        # Main stylesheet (1400+ lines)
│   │   ├── js/
│   │   │   └── script.js        # JavaScript logic
│   │   └── images/
│   │       └── bisma.jpeg       # Profile image
│   ├── templates/                # HTML templates
│   │   ├── base.html            # Base template
│   │   ├── home.html            # Landing page
│   │   ├── about.html           # About page
│   │   ├── projects.html        # Projects showcase
│   │   ├── blog.html            # Blog page
│   │   └── contact.html         # Contact form
│   ├── admin.py                  # Admin panel customization
│   ├── models.py                 # Database models (CV, Project, ContactMessage)
│   ├── views.py                  # View logic
│   ├── forms.py                  # Django forms
│   └── urls.py                   # App URL routing
├── myportfolio/                  # Project settings
│   ├── settings.py               # Django configuration
│   ├── urls.py                   # Main URL configuration
│   ├── wsgi.py                   # WSGI config
│   └── asgi.py                   # ASGI config
├── media/                        # User uploads
│   ├── cvs/                      # CV PDFs
│   └── projects/                 # Project images & PDFs
├── db.sqlite3                    # SQLite database
├── manage.py                     # Django CLI
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## 🎯 Key Features Explained

### 1. CV Management System
- Upload CV/resume as PDF through admin panel
- Add description text displayed on home page
- Auto-deactivates previous CVs when uploading new one
- Download button shown on home and about pages
- PDF validation ensures only PDF files accepted

### 2. Project Portfolio
- Create unlimited projects with detailed information
- Upload project image and optional PDF documentation
- Categorize by type: Frontend, Backend, Full Stack, Django
- Add comma-separated technologies list
- Link to live demo and GitHub repository
- Featured flag to highlight key projects (shown on home page)
- Custom ordering system

### 3. Contact Form
- AJAX-powered forms with real-time validation
- Email notifications sent to admin automatically
- All messages stored in database
- Mark messages as read/unread in admin
- XSS and CSRF protection built-in

### 4. Enhanced Admin Panel
- Image previews for projects
- PDF file links with direct view
- Searchable fields for easy navigation
- List filters for quick sorting
- Inline editing for featured status and ordering
- Collapsible timestamp sections
- Custom branding with portfolio name

## 📧 Email Configuration

### Development (Console Backend)
Already configured - emails print to console.

### Production (SMTP)
Edit `myportfolio/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-specific-password'
DEFAULT_FROM_EMAIL = 'noreply@yourdomain.com'
ADMIN_EMAIL = 'your-email@gmail.com'
```

**Gmail Setup:**
1. Enable 2-Factor Authentication
2. Generate App Password
3. Use App Password in settings

## 🎨 Customization Guide

### Personal Information
**Header & Branding:**
- Edit `main/templates/base.html` (lines 28-30) - Update name and navigation
- Edit `main/admin.py` (lines 113-115) - Admin panel titles

**Profile & Bio:**
- Replace `main/static/images/bisma.jpeg` with your photo
- Edit `main/templates/home.html` - Update name, role, description
- Edit `main/templates/about.html` - Update about section

### Styling & Colors
Colors defined in `main/static/css/style.css` (lines 1-50):

```css
:root {
    --primary: #8b5cf6;      /* Purple accent */
    --accent: #8b5cf6;
    --bg: #0a0b0d;           /* Dark background */
    --text-primary: #f8f9fa;
}
```

Modify these variables to change the entire color scheme.

### Content Management
1. Login to admin: `http://127.0.0.1:8000/admin/`
2. Add/edit projects under "Projects"
3. Upload CV under "CVs"
4. View contact messages under "Contact messages"

## 🚀 Production Deployment

### Environment Variables
Create `.env` file from `.env.example`:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgres://...
```

### Static Files
```bash
python manage.py collectstatic
```

###requirements.txt Included Packages
```
Django==5.2.7
Pillow==11.2.0
python-decouple==3.8
whitenoise==6.6.0
```

### Heroku Deployment (Quick)
```bash
heroku login
heroku create portfolio-app-name
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku open
```

### VPS/Server Deployment
1. Install Python 3.8+
2. Clone repository
3. Set up virtual environment
4. Install dependencies
5. Configure Nginx/Apache
6. Set up Gunicorn/uWSGI
7. Configure SSL with Let's Encrypt

## 📊 Database Models

### CV Model
```python
- title: CharField (CV name/title)
- description: TextField (shown above download button)
- file: FileField (PDF only)
- is_active: BooleanField (auto-manages active CV)
- uploaded_at: DateTimeField
- updated_at: DateTimeField
```

### Project Model
```python
- title: CharField (project name)
- description: TextField (project details)
- image: ImageField (project thumbnail)
- pdf_file: FileField (optional PDF documentation)
- category: CharField (Frontend/Backend/Full Stack/Django)
- technologies: CharField (comma-separated list)
- live_url: URLField (live demo link)
- github_url: URLField (source code link)
- featured: BooleanField (show on homepage)
- order: IntegerField (custom sorting)
- created_at: DateTimeField
- updated_at: DateTimeField
```

### ContactMessage Model
```python
- name: CharField (sender name)
- email: EmailField (sender email)
- message: TextField (message content)
- is_read: BooleanField (admin tracking)
- created_at: DateTimeField
```

## 🔧 Development Tips

### Custom Management Command
Quick setup with demo data:
```bash
python manage.py setup_portfolio
```

Creates:
- Superuser: admin/admin123
- 3 sample projects
- Demo data for testing

### Django Shell
```bash
python manage.py shell
```

Useful commands:
```python
from main.models import CV, Project, ContactMessage

CV.objects.filter(is_active=True).first()
Project.objects.filter(featured=True)
ContactMessage.objects.filter(is_read=False).count()
```

### Clear Database
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8080
```

### Static Files Not Loading
```bash
python manage.py collectstatic --clear
```

### Media Files Not Showing
Check `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

And `urls.py`:
```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Module Not Found
```bash
pip install -r requirements.txt
```

## 📝 Contributing

This is a personal portfolio project. Feel free to fork and customize for your own use.

### Development Workflow
1. Create feature branch
2. Make changes
3. Test thoroughly
4. Commit with meaningful messages
5. Push and create pull request

## 📜 License

This project showcases Django development skills and is available for learning purposes.

## 📧 Contact

- **Developer**: Muhammad Moueen
- **GitHub**: [@MuhammadMoueen](https://github.com/MuhammadMoueen)
- **Repository**: [django-mini-projects-portfolio](https://github.com/MuhammadMoueen/django-mini-projects-portfolio)

## 🙏 Acknowledgments

- Django Documentation
- Lucide Icons
- Google Fonts
- Python Community

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Python Documentation](https://docs.python.org/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

**Built with ❤️ using Django | Clean Code | Modern Design**

**⭐ Star this repo if you find it helpful!**
