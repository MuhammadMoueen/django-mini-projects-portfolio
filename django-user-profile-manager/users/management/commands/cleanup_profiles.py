from django.core.management.base import BaseCommand
from users.models import UserProfile

class Command(BaseCommand):
    help = 'Clean up profile pictures that no longer exist'

    def handle(self, *args, **kwargs):
        profiles = UserProfile.objects.all()
        cleaned = 0
        
        for profile in profiles:
            if profile.profile_picture:
                try:
                    profile.profile_picture.file
                except:
                    profile.profile_picture = None
                    profile.save()
                    cleaned += 1
                    self.stdout.write(self.style.SUCCESS(f'Cleaned profile for {profile.user.username}'))
        
        self.stdout.write(self.style.SUCCESS(f'Total profiles cleaned: {cleaned}'))
