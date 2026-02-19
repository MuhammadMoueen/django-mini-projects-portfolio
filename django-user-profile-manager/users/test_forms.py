from django.test import TestCase
from django.contrib.auth.models import User
from users.forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm

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
