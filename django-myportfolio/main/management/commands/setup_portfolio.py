from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from main.models import CV, Project, ContactMessage

User = get_user_model()


class Command(BaseCommand):
    help = 'Setup portfolio with initial data for demonstration'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('\n=== Portfolio Setup Started ===\n'))

        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('✓ Superuser created (username: admin, password: admin123)'))
        else:
            self.stdout.write(self.style.WARNING('✓ Superuser already exists'))

        # Create sample projects if none exist
        if Project.objects.count() == 0:
            projects_data = [
                {
                    'title': 'E-Commerce Platform',
                    'description': 'A full-featured e-commerce platform built with Django with payment integration and inventory management.',
                    'category': 'fullstack',
                    'technologies': 'Django, PostgreSQL, Stripe, HTML, CSS, JavaScript',
                    'featured': True,
                    'order': 1
                },
                {
                    'title': 'Blog Management System',
                    'description': 'Advanced blog platform with rich text editor, comments, and user authentication.',
                    'category': 'django',
                    'technologies': 'Django, SQLite, Bootstrap, CKEditor',
                    'featured': True,
                    'order': 2
                },
                {
                    'title': 'Portfolio Website',
                    'description': 'Modern responsive portfolio website with contact form and project showcase.',
                    'category': 'frontend',
                    'technologies': 'HTML, CSS, JavaScript, Django',
                    'featured': True,
                    'order': 3
                },
            ]

            for project_data in projects_data:
                Project.objects.create(**project_data)
            
            self.stdout.write(self.style.SUCCESS(f'✓ Created {len(projects_data)} sample projects'))
        else:
            self.stdout.write(self.style.WARNING(f'✓ Projects already exist ({Project.objects.count()} projects)'))

        self.stdout.write(self.style.SUCCESS('\n=== Setup Complete! ==='))
        self.stdout.write(self.style.SUCCESS('\nNext steps:'))
        self.stdout.write(self.style.SUCCESS('1. Run: python manage.py runserver'))
        self.stdout.write(self.style.SUCCESS('2. Visit: http://127.0.0.1:8000/admin/'))
        self.stdout.write(self.style.SUCCESS('3. Login with: admin / admin123'))
        self.stdout.write(self.style.SUCCESS('4. Upload your CV and add more projects!\n'))
