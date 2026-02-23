# Installation Guide

## Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

## Step-by-Step Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd django-blog-crud-system
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 6. Generate Sample Data (Optional)
```bash
python manage.py generate_sample_posts
```
This will create sample users and blog posts for testing.

### 7. Run Development Server
```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Post-Installation

### Access Points
- **Homepage**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Login**: http://127.0.0.1:8000/login/
- **Register**: http://127.0.0.1:8000/register/

### Default Accounts
If you used the sample data generator:
- Username: `admin` / Password: `admin123`
- Username: `john_doe` / Password: `testpass123`
- Username: `jane_smith` / Password: `testpass123`

## Troubleshooting

### Pillow Installation Issues
If you encounter issues installing Pillow:
```bash
# Windows
pip install Pillow --use-pep517

# Linux
sudo apt-get install python3-dev python3-setuptools
pip install Pillow
```

### Database Issues
If migrations fail:
```bash
python manage.py migrate --run-syncdb
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

## Production Deployment

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Set up proper static files serving
4. Use a production database (PostgreSQL recommended)
5. Configure HTTPS
6. Set up proper media files storage
