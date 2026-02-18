# 🔐 Django Authentication Dashboard System

A modern, professional Django authentication system with a beautiful dashboard interface, featuring dark/light theme toggle, responsive design, and comprehensive user management capabilities.

![Django](https://img.shields.io/badge/Django-5.0.1-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.2-purple?style=for-the-badge&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## ✨ Features

### 🔒 Authentication System
- **User Registration** - Complete signup form with email validation
- **User Login** - Secure authentication with Django's built-in auth system
- **User Logout** - Safe session termination
- **Password Management** - No restrictions for easy development
- **Session Handling** - Automatic session management

### 📊 Dashboard Interface
- **Protected Dashboard** - Login-required access with authentication decorators
- **Real-time Metrics** - Display account status, security score, and session info
- **Profile Summary** - Quick overview of user information
- **Account Overview** - Detailed user data display with organized grid layout
- **Quick Actions** - One-click access to common tasks

### 🎨 Modern UI/UX
- **Dark/Light Theme Toggle** - Persistent theme selection with localStorage
- **Smooth Animations** - Fade-in effects, hover transitions, and CSS animations
- **Responsive Design** - Mobile-first design with multiple breakpoints
- **Gradient Effects** - Modern color gradients and glassmorphism
- **Bootstrap Icons** - Professional icon set throughout the interface
- **Form Validation Styles** - Visual feedback for valid/invalid inputs

### ♿ Accessibility & Performance
- **ARIA Labels** - Screen reader support for better accessibility
- **Semantic HTML** - Proper HTML5 structure
- **SEO Optimized** - Meta tags and proper document structure
- **Performance Optimized** - CSS `will-change` properties for smooth animations
- **Cross-browser Compatible** - Works on all modern browsers

---

## 🛠️ Technologies Used

| Category | Technology |
|----------|-----------|
| **Backend Framework** | Django 5.0.1 |
| **Frontend Framework** | Bootstrap 5.3.2 |
| **Programming Language** | Python 3.x |
| **Database** | SQLite3 |
| **Icons** | Bootstrap Icons 1.11.3 |
| **Styling** | CSS3 with CSS Variables |
| **JavaScript** | Vanilla JS (ES6+) |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

```
django-auth-dashboard-system/
│
├── auth_dashboard/              # Main project directory
│   ├── __init__.py
│   ├── settings.py             # Project settings
│   ├── urls.py                 # URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── users/                       # Users app directory
│   ├── migrations/             # Database migrations
│   ├── static/                 # Static files
│   │   ├── css/
│   │   │   └── style.css       # Main stylesheet (860+ lines)
│   │   └── js/
│   │       └── theme.js        # Theme toggle functionality
│   ├── templates/              # HTML templates
│   │   ├── base.html           # Base template with navbar & footer
│   │   └── users/
│   │       ├── signup.html     # Registration page
│   │       ├── login.html      # Login page
│   │       ├── dashboard.html  # Main dashboard
│   │       └── profile.html    # User profile page
│   ├── __init__.py
│   ├── admin.py                # Custom admin configuration
│   ├── apps.py                 # App configuration
│   ├── forms.py                # Custom auth forms
│   ├── models.py               # User models (if extended)
│   ├── urls.py                 # App-specific URLs
│   └── views.py                # View functions
│
├── db.sqlite3                   # SQLite database
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation

```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/MuhammadMoueen/django-mini-projects-portfolio.git
cd django-mini-projects-portfolio/django-auth-dashboard-system
```

2. **Create a virtual environment** (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply database migrations**
```bash
python manage.py migrate
```

5. **Create a superuser** (optional, for admin access)
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

7. **Open your browser**
   - Visit: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

---

## 📖 Usage

### User Registration
1. Navigate to the signup page
2. Fill in username, email, and password
3. Click "Sign Up" to create your account
4. Automatically redirected to dashboard

### User Login
1. Go to the login page
2. Enter your credentials
3. Click "Login" to access your dashboard

### Dashboard Features
- **View Metrics**: See your account status, security score, and session info
- **Profile Summary**: Quick view of your user information
- **Account Overview**: Detailed breakdown of your account details
- **Quick Actions**: Access Edit Profile, Security Settings, Notifications, and Logout

### Theme Toggle
- Click the moon/sun icon in the navbar to switch between dark and light themes
- Your preference is saved automatically in browser localStorage

---

## 🎨 UI Features

### Color Scheme
- **Primary**: Indigo gradients (#6366f1)
- **Success**: Green shades (#10b981)
- **Info**: Blue tones (#3b82f6)
- **Warning**: Amber hues (#f59e0b)
- **Danger**: Red gradients (#ef4444)

### Components
- Gradient buttons with hover effects
- Metric cards with animated indicators
- Profile avatar with status badges
- Responsive navigation bar
- Glassmorphism effects
- Smooth page transitions
- Form validation feedback

### Responsive Breakpoints
- Mobile: < 576px
- Tablet: 576px - 768px
- Desktop: 768px - 992px
- Large Desktop: > 992px

---

## ⚙️ Configuration

### Settings Customization

Edit `auth_dashboard/settings.py` to customize:

```python
# Password validation (currently disabled for development)
AUTH_PASSWORD_VALIDATORS = []

# Login redirect
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'

# Allowed hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Static files
STATIC_URL = 'static/'
```

### Custom Styling

Modify `users/static/css/style.css` to change:
- CSS variables for colors
- Component styles
- Animations and transitions
- Responsive breakpoints

---

## 🔧 Development

### Adding New Features
1. Create new views in `users/views.py`
2. Add URL patterns in `users/urls.py`
3. Create templates in `users/templates/users/`
4. Add any required models in `users/models.py`
5. Run migrations if models changed

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files (Production)
```bash
python manage.py collectstatic
```

---

## 📸 Screenshots

> Add screenshots of your dashboard, login page, signup page, and profile page here

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Muhammad Moueen**
- GitHub: [@MuhammadMoueen](https://github.com/MuhammadMoueen)
- Email: muhammadmoueen5@gmail.com

---

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Framework
- Bootstrap Icons
- Python Community
- All contributors and supporters

---

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Python Documentation](https://docs.python.org/)
- [GitHub Repository](https://github.com/MuhammadMoueen/django-mini-projects-portfolio)

---

## 🐛 Known Issues

No known issues at this time. If you find any bugs, please open an issue on GitHub.

---

## 🔮 Future Enhancements

- [ ] Email verification system
- [ ] Password reset functionality
- [ ] Two-factor authentication (2FA)
- [ ] User profile picture upload
- [ ] Activity log and audit trail
- [ ] API endpoints with Django REST Framework
- [ ] Social authentication (Google, GitHub, etc.)
- [ ] Advanced user roles and permissions
- [ ] Notification system
- [ ] User settings page

---

<div align="center">

### ⭐ If you like this project, please give it a star on GitHub! ⭐

Made with ❤️ by Muhammad Moueen

</div>
