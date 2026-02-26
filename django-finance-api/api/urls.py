from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'incomes', views.IncomeViewSet, basename='income')
router.register(r'expenses', views.ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', views.login_page, name='login'),
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup_page, name='signup_page'),
    path('dashboard/', views.dashboard_page, name='dashboard'),
    path('categories/', views.categories_page, name='categories'),
    path('edit-profile/', views.edit_profile_page, name='edit_profile'),
    path('change-password/', views.change_password_page, name='change_password'),
    
    path('api/auth/register/', views.register, name='register'),
    path('api/auth/login/', views.login, name='api_login'),
    path('api/auth/logout/', views.logout, name='logout'),
    path('api/auth/profile/', views.profile, name='profile'),
    path('api/auth/profile/update/', views.update_profile, name='update_profile'),
    path('api/auth/change-password/', views.change_password, name='change_password'),
    
    path('api/summary/', views.financial_summary, name='financial_summary'),
    path('api/monthly-report/', views.monthly_report, name='monthly_report'),
    path('api/category-report/', views.category_report, name='category_report'),
    
    path('api/', include(router.urls)),
]


