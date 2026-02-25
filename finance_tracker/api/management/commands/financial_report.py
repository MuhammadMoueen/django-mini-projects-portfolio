from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db.models import Sum
from api.models import Income, Expense
from datetime import datetime

class Command(BaseCommand):
    help = 'Generate financial report for a user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username to generate report for')
        parser.add_argument(
            '--year',
            type=int,
            default=datetime.now().year,
            help='Year for the report'
        )

    def handle(self, *args, **options):
        username = options['username']
        year = options['year']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User {username} not found'))
            return

        incomes = Income.objects.filter(user=user, date__year=year)
        expenses = Expense.objects.filter(user=user, date__year=year)

        total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
        total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0
        balance = total_income - total_expense

        self.stdout.write(self.style.SUCCESS(f'\n=== Financial Report for {username} ({year}) ===\n'))
        self.stdout.write(f'Total Income:  ${total_income:,.2f}')
        self.stdout.write(f'Total Expense: ${total_expense:,.2f}')
        self.stdout.write(f'Net Balance:   ${balance:,.2f}')
        
        if balance >= 0:
            self.stdout.write(self.style.SUCCESS(f'\nYou saved: ${balance:,.2f}'))
        else:
            self.stdout.write(self.style.ERROR(f'\nYou overspent by: ${abs(balance):,.2f}'))

        self.stdout.write(f'\nTotal Transactions: {incomes.count() + expenses.count()}')
        self.stdout.write(f'  - Income entries: {incomes.count()}')
        self.stdout.write(f'  - Expense entries: {expenses.count()}')

        income_by_cat = incomes.values('category__name').annotate(
            total=Sum('amount')
        ).order_by('-total')[:5]

        if income_by_cat:
            self.stdout.write(self.style.SUCCESS('\nTop Income Categories:'))
            for item in income_by_cat:
                self.stdout.write(f"  - {item['category__name']}: ${item['total']:,.2f}")

        expense_by_cat = expenses.values('category__name').annotate(
            total=Sum('amount')
        ).order_by('-total')[:5]

        if expense_by_cat:
            self.stdout.write(self.style.WARNING('\nTop Expense Categories:'))
            for item in expense_by_cat:
                self.stdout.write(f"  - {item['category__name']}: ${item['total']:,.2f}")

        self.stdout.write('\n')
