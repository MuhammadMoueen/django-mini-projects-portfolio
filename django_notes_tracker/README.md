# Django Notes Tracker 📝

A clean, modern, and production-ready Django application for managing personal notes with full CRUD functionality.

![Django](https://img.shields.io/badge/Django-5.0-green.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)

## 🌟 Features

- **Create Notes**: Add new notes with title and content
- **View Notes**: Display all notes on the homepage with search functionality
- **View Details**: View individual notes with full content and statistics
- **Delete Notes**: Remove notes with confirmation modal
- **Search**: Search notes by title or content
- **Responsive UI**: Modern, gradient-based design with Bootstrap 5
- **Clean Architecture**: Well-organized code following Django best practices
- **Production-Ready**: Proper structure with migrations, tests, and documentation

## 📸 Screenshots

### Homepage - Notes List
Beautiful gradient design with all your notes displayed in cards, showing title, preview, and creation date.

### Add Note Form
Clean form with validation and character counter for creating new notes.

### Note Detail View
Full note display with statistics including character count and word count.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Installation

1. **Navigate to the project directory**
   ```bash
   cd django_notes_tracker
   ```

2. **Create and activate virtual environment**
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

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Visit the application**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📁 Project Structure

```
django_notes_tracker/
├── django_notes_tracker/       # Main project configuration
│   ├── __init__.py
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main URL configuration
│   ├── wsgi.py                # WSGI configuration
│   └── asgi.py                # ASGI configuration
├── notes/                      # Notes application
│   ├── migrations/            # Database migrations
│   ├── __init__.py
│   ├── admin.py               # Admin panel configuration
│   ├── apps.py                # App configuration
│   ├── models.py              # Note model
│   ├── tests.py               # Unit tests
│   ├── urls.py                # App URL patterns
│   └── views.py               # View functions
├── templates/                  # HTML templates
│   ├── base.html              # Base template with Bootstrap
│   └── notes/
│       ├── home.html          # Homepage with notes list
│       ├── add_note.html      # Add note form
│       └── view_note.html     # Note detail view
├── static/                     # Static files (CSS, JS, images)
│   └── custom.css             # Custom styles
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── db.sqlite3                 # SQLite database (created after migrations)
└── README.md                   # This file
```

## 🎯 Usage

### Creating a Note

1. Click on **"Add Note"** in the navigation bar or the **"Create New Note"** button on the homepage
2. Enter a descriptive title (max 200 characters)
3. Write your note content in the text area
4. Click **"Save Note"** to create the note
5. You'll be redirected to the homepage with a success message

### Viewing Notes

- All notes are displayed on the **homepage** in reverse chronological order (newest first)
- Each note card shows:
  - Title
  - Content preview (first 100 characters)
  - Creation date
  - Action buttons (View, Delete)

### Viewing Full Note

1. Click **"View Full Note"** button on any note card
2. See the complete note with:
   - Full title and content
   - Creation date and time
   - Statistics (character count, word count)
   - Action buttons

### Searching Notes

1. Use the **search bar** on the homepage
2. Enter keywords to search in both titles and content
3. Click **"Search"** to filter notes
4. Click **"Clear"** to reset and show all notes

### Deleting Notes

1. Click the **"Delete"** button on any note card
2. Confirm deletion in the modal dialog
3. The note will be permanently removed from the database

## 🔧 Django Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/` to:

- View all notes in a detailed list view
- Search notes by title or content
- Filter notes by creation date
- Add, edit, or delete notes directly
- View content previews in the list

**Note**: You need to create a superuser account first using:
```bash
python manage.py createsuperuser
```

## 🧪 Running Tests

The project includes a comprehensive test suite covering:
- Note model creation and methods
- View functionality
- CRUD operations
- Form validation

To run the tests:
```bash
python manage.py test notes
```

For verbose output:
```bash
python manage.py test notes --verbosity=2
```

## 🎨 Customization

### Changing Theme Colors

Edit the CSS variables in `templates/base.html`:

```css
:root {
    --primary-color: #6366f1;      /* Primary purple */
    --secondary-color: #8b5cf6;    /* Secondary purple */
    --success-color: #10b981;      /* Success green */
    --danger-color: #ef4444;       /* Danger red */
    --dark-color: #1f2937;         /* Dark gray */
    --light-color: #f9fafb;        /* Light gray */
}
```

### Modifying the Note Model

1. Edit `notes/models.py`
2. Make your changes to the Note model
3. Create and apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Adding New Fields

Example - Adding a category field:

1. Update the model in `notes/models.py`:
   ```python
   category = models.CharField(max_length=50, default='General')
   ```

2. Update forms and templates accordingly
3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## 📚 Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend Framework** | Django 5.0 |
| **Database** | SQLite3 |
| **Frontend** | HTML5, CSS3, JavaScript |
| **CSS Framework** | Bootstrap 5.3 |
| **Icons** | Bootstrap Icons |
| **Python Version** | 3.8+ |

## 🔒 Security Features

- ✅ CSRF protection on all forms
- ✅ SQL injection prevention (Django ORM)
- ✅ XSS protection (Django template escaping)
- ✅ Secure password hashing (for admin users)
- ✅ Form validation and sanitization

## 📝 API Endpoints

| URL Pattern | View Function | HTTP Method | Purpose |
|-------------|---------------|-------------|---------|
| `/` | `home` | GET | Display all notes with optional search |
| `/add/` | `add_note` | GET, POST | Display form and create new note |
| `/note/<id>/` | `view_note` | GET | View single note details |
| `/delete/<id>/` | `delete_note` | POST | Delete a note |

## 🚀 Deployment Checklist

Before deploying to production:

### Essential Steps

1. **Security Settings**
   - Set `DEBUG = False` in `settings.py`
   - Configure `ALLOWED_HOSTS` with your domain
   - Use environment variables for `SECRET_KEY`

2. **Database**
   - Migrate to PostgreSQL or MySQL for production
   - Configure database connection settings
   - Run migrations on production database

3. **Static Files**
   - Run `python manage.py collectstatic`
   - Configure static file serving (use Whitenoise or CDN)
   - Set proper `STATIC_ROOT` and `STATIC_URL`

4. **Security Headers**
   - Enable HTTPS
   - Set `SECURE_SSL_REDIRECT = True`
   - Configure `SECURE_HSTS_SECONDS`
   - Set `SESSION_COOKIE_SECURE = True`
   - Set `CSRF_COOKIE_SECURE = True`

5. **Error Handling**
   - Configure proper logging
   - Set up error email notifications
   - Create custom error pages (404, 500)

6. **Performance**
   - Enable database connection pooling
   - Configure caching (Redis/Memcached)
   - Optimize database queries

### Recommended Platforms

- **Heroku**: Easy deployment with PostgreSQL add-on
- **PythonAnywhere**: Python-focused hosting
- **DigitalOcean**: VPS with full control
- **AWS/Azure/GCP**: Enterprise-grade cloud platforms
- **Railway/Render**: Modern deployment platforms

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed
- Comment your code where necessary

## 🐛 Known Issues & Limitations

- Currently supports only single-user mode (no multi-user authentication)
- No note editing functionality (only create, view, delete)
- No note categories or tags
- No file attachments support
- No rich text editor (plain text only)

### Planned Features

- [ ] Note editing functionality
- [ ] User authentication and multi-user support
- [ ] Note categories and tags
- [ ] Rich text editor (Markdown support)
- [ ] File attachments
- [ ] Note sharing functionality
- [ ] Export notes (PDF, TXT)
- [ ] Dark mode toggle

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Muhammad Moueen**

- GitHub: [@MuhammadMoueen](https://github.com/MuhammadMoueen)
- Project Repository: [django-mini-projects-portfolio](https://github.com/MuhammadMoueen/django-mini-projects-portfolio)

## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/) - Excellent framework documentation
- [Bootstrap Team](https://getbootstrap.com/) - Beautiful responsive framework
- [Bootstrap Icons](https://icons.getbootstrap.com/) - Comprehensive icon library
- Django Community - For amazing tutorials and support

## 📞 Support

If you have any questions or run into issues:

1. Check the [Django documentation](https://docs.djangoproject.com/)
2. Search existing issues on GitHub
3. Create a new issue with detailed information
4. Reach out via the contact information above

---

**Happy Coding! 🎉**

If you find this project helpful, please give it a ⭐️ on GitHub!

Made with ❤️ using Django and Bootstrap
