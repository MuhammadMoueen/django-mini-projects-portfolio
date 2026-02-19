from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import UserProfile

class Command(BaseCommand):
    help = 'Create demo users for testing'

    def handle(self, *args, **kwargs):
        demo_users = [
            {'username': 'john_doe', 'email': 'john@example.com', 'password': 'demo1234'},
            {'username': 'jane_smith', 'email': 'jane@example.com', 'password': 'demo1234'},
            {'username': 'bob_jones', 'email': 'bob@example.com', 'password': 'demo1234'},
        ]

        for user_data in demo_users:
            if not User.objects.filter(username=user_data['username']).exists():
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password']
                )
                user.profile.full_name = user_data['username'].replace('_', ' ').title()
                user.profile.bio = f"This is a demo profile for {user_data['username']}"
                user.profile.save()
                self.stdout.write(self.style.SUCCESS(f'Created user: {user_data["username"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'User already exists: {user_data["username"]}'))
