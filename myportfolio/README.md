# Muhammad Moueen - Professional Portfolio

A modern, professional Django-based portfolio website showcasing projects, skills, and contact information.

## ✨ Features

- **Dynamic Project Showcase**: Display projects with images, descriptions, and links
- **CV Download System**: Upload and manage CV/resume with download functionality
- **Contact Form**: AJAX-powered contact form with email notifications
- **Admin Dashboard**: Easy content management through Django admin
- **Responsive Design**: Mobile-first, fully responsive design
- **Dark Mode**: Professional dark theme with smooth animations
- **Email Integration**: Automatic email notifications for contact messages

## 🚀 Technologies Used

- **Backend**: Django 5.0+, Python 3.x
- **Frontend**: HTML5, CSS3 (Custom), Vanilla JavaScript
- **Database**: SQLite (Development)
- **Icons**: Lucide Icons
- **Email**: Django Email Backend

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/MuhammadMoueen/django-mini-projects-portfolio.git
cd django-mini-projects-portfolio/myportfolio
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Run development server**
```bash
python manage.py runserver
```

7. **Access the application**
- Portfolio: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
myportfolio/
├── main/                      # Main app
│   ├── migrations/           # Database migrations
│   ├── static/              # Static files
│   │   ├── css/            # Stylesheets
│   │   ├── js/             # JavaScript files
│   │   └── images/         # Images
│   ├── templates/          # HTML templates
│   ├── admin.py           # Admin configuration
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Form definitions
│   └── urls.py            # URL routing
├── myportfolio/            # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── media/                 # User-uploaded files
├── db.sqlite3            # Database
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## 🎨 Features Overview

### 1. Project Management
- Add projects through Django admin
- Upload project images
- Categorize projects (Frontend, Backend, Full Stack, Django)
- Add technologies used
- Link to live demo and GitHub repository
- Feature important projects on homepage

### 2. CV/Resume System
- Upload PDF CV/resume
- Mark active CV for download
- Download button on homepage and about page
- Automatic deactivation of previous CVs

### 3. Contact System
- Client-side and server-side validation
- AJAX form submission
- Email notifications to admin
- Messages stored in database
- Mark messages as read/unread

### 4. Admin Panel
- Manage projects
- Upload CV
- View contact messages
- Mark messages as read
- Full CRUD operations

## 📧 Email Configuration

For production, update `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## 🎯 Customization

### Update Personal Information
1. Edit `base.html` to update name and links
2. Update contact information in `contact.html`
3. Add your profile picture to `static/images/`
4. Update skills in `about.html`

### Styling
- Main styles: `main/static/css/style.css`
- Colors are defined as CSS variables in `:root`
- Modify variables for theme customization

## 🚀 Deployment

### Heroku Deployment
```bash
# Install Heroku CLI
heroku create your-app-name
heroku config:set DJANGO_SETTINGS_MODULE=myportfolio.settings
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Environment Variables
Set these for production:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False
- `ALLOWED_HOSTS`: Add your domain

## 📝 Models

### CV Model
- title: CV title/version
- file: PDF file upload
- is_active: Active CV flag
- uploaded_at: Upload timestamp

### Project Model
- title: Project name
- description: Project description
- image: Project screenshot
- category: Project type
- technologies: Tech stack
- live_url: Demo link
- github_url: Repository link
- featured: Featured flag
- order: Display order

### ContactMessage Model
- name: Sender name
- email: Sender email
- message: Message content
- created_at: Timestamp
- is_read: Read status

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Muhammad Moueen**
- GitHub: [@MuhammadMoueen](https://github.com/MuhammadMoueen)
- LinkedIn: [Muhammad Moueen](https://linkedin.com/in/muhammadmoueen)
- Email: muhammadmoueen@gmail.com

## 🙏 Acknowledgments

- Lucide Icons for beautiful iconography
- Django community for excellent documentation
- Google Fonts for typography

---

Made with ❤️ by Muhammad Moueen
