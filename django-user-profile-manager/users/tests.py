from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile
from .forms import UserRegisterForm, ProfileUpdateForm

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

class AuthenticationViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
    
    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
    
    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
    
    def test_login_success(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass123'})
        self.assertEqual(response.status_code, 302)
    
    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
    
    def test_dashboard_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

class FormsTest(TestCase):
    def test_register_form_valid(self):
        form_data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_register_form_duplicate_email(self):
        User.objects.create_user(username='existing', email='test@example.com', password='pass123')
        form_data = {
            'username': 'newuser',
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_profile_form_valid(self):
        form_data = {
            'full_name': 'Test User',
            'bio': 'This is a test bio',
            'phone': '+1234567890',
            'location': 'Test City'
        }
        form = ProfileUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())
