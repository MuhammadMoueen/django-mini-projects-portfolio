# Blog CRUD System

A professional Django blog application with full CRUD functionality and user authentication. Built with clean architecture, modern UI design, and production-ready features.

## Features

### Authentication System
- User registration with email validation
- Secure login and logout
- Password validation with Django built-in validators
- Automatic user profile creation

### Blog Management
- Create, read, update, and delete blog posts
- Rich text content support with proper formatting
- Character counter for title and content fields
- Form validation (minimum length requirements)
- Post timestamps (created and updated dates)

### User Experience
- Modern responsive UI with gradient theme
- Bootstrap 5 integration
- Dark and white theme combination
- Mobile-friendly design
- Smooth scrolling and animations
- Custom 404 error page
- Breadcrumb navigation
- Search functionality (by title, content, or author)
- Sorting options (newest, oldest, by title)
- Pagination for post listings

### Permissions & Security
- Only authenticated users can create posts
- Users can only edit/delete their own posts
- Admin/superuser can manage all posts
- Guest users can read all posts
- Protected routes with login_required decorator
- CSRF protection on all forms

### Additional Features
- Author profile pages showing all posts by an author
- User dashboard with statistics
- Post count tracking
- Weekly activity metrics
- Recently updated post indicators
- Author avatar circles
- Management command for generating sample data

## Project Structure

```
blog-crud-system/
├── blog/
│   ├── management/
│   │   └── commands/
│   │       └── generate_sample_posts.py
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   ├── blog/
│   │   │   ├── author_posts.html
│   │   │   ├── dashboard.html
│   │   │   ├── home.html
│   │   │   ├── login.html
│   │   │   ├── post_confirm_delete.html
│   │   │   ├── post_detail.html
│   │   │   ├── post_form.html
│   │   │   └── register.html
│   │   ├── 404.html
│   │   └── base.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blog_system/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

## Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd blog-crud-system
```

2. **Create a virtual environment:**
```bash
python -m venv venv
```

3. **Activate the virtual environment:**
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Run migrations:**
```bash
python manage.py migrate
```

6. **Create a superuser (optional):**
```bash
python manage.py createsuperuser
```

7. **Generate sample data (optional):**
```bash
python manage.py generate_sample_posts
```

8. **Run the development server:**
```bash
python manage.py runserver
```

9. **Access the application:**
- Main site: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### For Regular Users

1. **Register an account** at `/register/`
2. **Login** at `/login/`
3. **View all posts** on the home page
4. **Search posts** using the search bar
5. **Sort posts** by newest, oldest, or by title
6. **Create a new post** from the dashboard or navigation
7. **Edit/Delete your posts** from post detail page or dashboard
8. **View author profiles** to see all posts by a specific user

### For Administrators

1. **Access admin panel** at `/admin/`
2. **Manage all posts** including editing and deleting
3. **View user profiles** and statistics
4. **Monitor post creation dates** and updates

## Models

### Post Model
- `title`: CharField (max 200 characters)
- `content`: TextField
- `author`: ForeignKey to User
- `created_at`: DateTimeField (auto)
- `updated_at`: DateTimeField (auto)

### UserProfile Model
- `user`: OneToOneField to User
- `bio`: TextField (max 500 characters, optional)
- `created_at`: DateTimeField (auto)

## Tech Stack

- **Backend:** Django 4.2+
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Bootstrap 5, Custom CSS
- **Authentication:** Django built-in auth system

## Key Features Implementation

### Clean Code Practices
- No comments or docstrings (as per requirements)
- Clear variable and function naming
- Proper separation of concerns
- DRY principles applied
- Modular template structure

### Security Features
- Password hashing with Django's auth system
- CSRF protection on forms
- XSS prevention through template escaping
- SQL injection prevention with ORM
- User permission checks on sensitive operations

### Performance Optimization
- Database query optimization
- Pagination to reduce load time
- Efficient template inheritance
- Minimal external dependencies

## Development Commits

This project was built with 46+ meaningful commits covering:
1. Initial project setup
2. Model creation and migrations
3. Form development with validation
4. View implementation with permissions
5. Template design and styling
6. Feature additions (search, sort, profiles)
7. UI/UX improvements
8. Security enhancements
9. Documentation updates
10. Final polish and bug fixes

## Contributing

This is a portfolio project demonstrating professional Django development practices.

## License

This project is part of the django-mini-projects-portfolio repository.

---

**Built with Django | Clean Architecture | Modern Design**
