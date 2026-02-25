from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from decimal import Decimal
from datetime import date
from .models import Category, Income, Expense

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/api/auth/register/'
        self.login_url = '/api/auth/login/'

    def test_user_registration(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'password2': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

    def test_user_login(self):
        User.objects.create_user(username='testuser', password='testpass123')
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

class CategoryTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_category(self):
        data = {'name': 'Salary', 'category_type': 'income'}
        response = self.client.post('/api/categories/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_categories(self):
        Category.objects.create(user=self.user, name='Salary', category_type='income')
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class IncomeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(
            user=self.user, name='Salary', category_type='income'
        )

    def test_create_income(self):
        data = {
            'amount': '1000.00',
            'date': str(date.today()),
            'category': self.category.id,
            'notes': 'Test income'
        }
        response = self.client.post('/api/incomes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_amount(self):
        data = {
            'amount': '-100.00',
            'date': str(date.today()),
            'category': self.category.id
        }
        response = self.client.post('/api/incomes/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ExpenseTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(
            user=self.user, name='Food', category_type='expense'
        )

    def test_create_expense(self):
        data = {
            'amount': '50.00',
            'date': str(date.today()),
            'category': self.category.id,
            'notes': 'Test expense'
        }
        response = self.client.post('/api/expenses/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class FinancialSummaryTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        income_cat = Category.objects.create(user=self.user, name='Salary', category_type='income')
        expense_cat = Category.objects.create(user=self.user, name='Food', category_type='expense')
        
        Income.objects.create(user=self.user, category=income_cat, amount=Decimal('1000'), date=date.today())
        Expense.objects.create(user=self.user, category=expense_cat, amount=Decimal('200'), date=date.today())

    def test_financial_summary(self):
        response = self.client.get('/api/summary/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_income'], 1000.0)
        self.assertEqual(response.data['total_expense'], 200.0)
        self.assertEqual(response.data['balance'], 800.0)

