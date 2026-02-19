from django.test import TestCase
from django.contrib.auth.models import User
from users.models import UserProfile

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
    
    def test_profile_creation(self):
        self.assertTrue(hasattr(self.user, 'profile'))
        self.assertIsInstance(self.user.profile, UserProfile)
    
    def test_profile_str(self):
        expected_str = f"{self.user.username}'s Profile"
        self.assertEqual(str(self.user.profile), expected_str)
    
    def test_profile_completion_empty(self):
        self.assertEqual(self.user.profile.profile_completion_percentage, 0)
    
    def test_profile_completion_partial(self):
        profile = self.user.profile
        profile.full_name = "Test User"
        profile.bio = "Test bio"
        profile.save()
        self.assertEqual(profile.profile_completion_percentage, 40)
