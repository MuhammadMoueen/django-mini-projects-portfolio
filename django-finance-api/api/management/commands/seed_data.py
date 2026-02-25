from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta, date
from decimal import Decimal
import random
from api.models import Category, Income, Expense
from api.constants import DEFAULT_INCOME_CATEGORIES, DEFAULT_EXPENSE_CATEGORIES

class Command(BaseCommand):
    help = 'Seed database with sample financial data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='testuser',
            help='Username for sample data'
        )
        parser.add_argument(
            '--months',
            type=int,
            default=3,
            help='Number of months of data to generate'
        )

    def handle(self, *args, **options):
        username = options['username']
        months = options['months']

        user, created = User.objects.get_or_create(
            username=username,
            defaults={'email': f'{username}@example.com'}
        )
        
        if created:
            user.set_password('password123')
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Created user: {username}'))
        else:
            self.stdout.write(self.style.WARNING(f'User {username} already exists'))

        income_categories = []
        for cat_name in DEFAULT_INCOME_CATEGORIES:
            cat, _ = Category.objects.get_or_create(
                user=user,
                name=cat_name,
                category_type='income'
            )
            income_categories.append(cat)

        expense_categories = []
        for cat_name in DEFAULT_EXPENSE_CATEGORIES:
            cat, _ = Category.objects.get_or_create(
                user=user,
                name=cat_name,
                category_type='expense'
            )
            expense_categories.append(cat)

        self.stdout.write(self.style.SUCCESS(f'Created categories'))

        today = date.today()
        income_count = 0
        expense_count = 0

        for month_offset in range(months):
            current_date = today - timedelta(days=30 * month_offset)
            
            for _ in range(random.randint(2, 5)):
                Income.objects.create(
                    user=user,
                    category=random.choice(income_categories),
                    amount=Decimal(random.uniform(500, 5000)).quantize(Decimal('0.01')),
                    date=current_date - timedelta(days=random.randint(0, 28)),
                    notes=f'Sample income for {current_date.strftime("%B %Y")}'
                )
                income_count += 1

            for _ in range(random.randint(5, 15)):
                Expense.objects.create(
                    user=user,
                    category=random.choice(expense_categories),
                    amount=Decimal(random.uniform(10, 1000)).quantize(Decimal('0.01')),
                    date=current_date - timedelta(days=random.randint(0, 28)),
                    notes=f'Sample expense for {current_date.strftime("%B %Y")}'
                )
                expense_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {income_count} incomes and {expense_count} expenses'
            )
        )
