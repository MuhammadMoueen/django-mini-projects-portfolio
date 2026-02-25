from django.db import models
from django.contrib.auth.models import User
from .constants import INCOME_TYPE, EXPENSE_TYPE, CATEGORY_TYPES, MAX_AMOUNT


class Category(models.Model):
    """
    Category model for organizing income and expense transactions.
    Each user can create their own categories for better financial organization.
    """
    INCOME = INCOME_TYPE
    EXPENSE = EXPENSE_TYPE
    
    CATEGORY_TYPES = CATEGORY_TYPES
    
    name = models.CharField(max_length=100)
    category_type = models.CharField(max_length=10, choices=CATEGORY_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
        unique_together = ['user', 'name', 'category_type']

    def __str__(self):
        return f"{self.name} ({self.category_type})"

class Income(models.Model):
    """
    Income model to track all income transactions.
    Links to user and optional category for detailed financial tracking.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='incomes')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name_plural = 'Incomes'

    def __str__(self):
        return f"{self.amount} on {self.date}"

class Expense(models.Model):
    """
    Expense model to track all expense transactions.
    Supports categorization and detailed notes for spending analysis.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='expenses')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return f"{self.amount} on {self.date}"

