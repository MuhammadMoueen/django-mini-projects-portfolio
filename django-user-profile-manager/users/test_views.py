from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

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
