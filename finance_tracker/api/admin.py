from django.contrib import admin
from .models import Category, Income, Expense

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'user', 'created_at']
    list_filter = ['category_type', 'created_at']
    search_fields = ['name', 'user__username']
    readonly_fields = ['created_at']
    ordering = ['name']

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['amount', 'category', 'date', 'user', 'created_at']
    list_filter = ['category', 'date', 'created_at']
    search_fields = ['notes', 'user__username']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'date'
    ordering = ['-date']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['amount', 'category', 'date', 'user', 'created_at']
    list_filter = ['category', 'date', 'created_at']
    search_fields = ['notes', 'user__username']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'date'
    ordering = ['-date']

