from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Generate profile statistics report'

    def handle(self, *args, **kwargs):
        total_users = User.objects.count()
        active_users = User.objects.filter(is_active=True).count()
        
        profiles_with_pic = User.objects.filter(profile__profile_picture__isnull=False).count()
        profiles_with_bio = User.objects.exclude(profile__bio='').count()
        profiles_with_phone = User.objects.exclude(profile__phone='').count()
        
        self.stdout.write(self.style.SUCCESS('=== Profile Statistics ==='))
        self.stdout.write(f'Total Users: {total_users}')
        self.stdout.write(f'Active Users: {active_users}')
        self.stdout.write(f'Profiles with Picture: {profiles_with_pic}')
        self.stdout.write(f'Profiles with Bio: {profiles_with_bio}')
        self.stdout.write(f'Profiles with Phone: {profiles_with_phone}')
        self.stdout.write(self.style.SUCCESS('=========================='))
