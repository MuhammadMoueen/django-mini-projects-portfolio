from django.contrib.auth import authenticate
from django.shortcuts import render
from django.db.models import Sum, Q
from datetime import datetime, timedelta
from rest_framework import status, viewsets, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Category, Income, Expense
from .serializers import (
    UserRegistrationSerializer, UserLoginSerializer, UserSerializer,
    CategorySerializer, IncomeSerializer, ExpenseSerializer
)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key,
            'message': 'Registration successful'
        }, status=status.HTTP_201_CREATED)
    return Response({
        'errors': serializer.errors,
        'message': 'Registration failed'
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserSerializer(user).data,
                'token': token.key,
                'message': 'Login successful'
            })
        return Response({
            'error': 'Invalid credentials',
            'message': 'Username or password is incorrect'
        }, status=status.HTTP_401_UNAUTHORIZED)
    return Response({
        'errors': serializer.errors,
        'message': 'Invalid input'
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({'message': 'Successfully logged out'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']

    def get_queryset(self):
        queryset = Category.objects.filter(user=self.request.user)
        category_type = self.request.query_params.get('type', None)
        if category_type:
            queryset = queryset.filter(category_type=category_type)
        return queryset

class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['notes']
    ordering_fields = ['date', 'amount', 'created_at']

    def get_queryset(self):
        queryset = Income.objects.filter(user=self.request.user)
        
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category_id=category)
        
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
        
        return queryset

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['notes']
    ordering_fields = ['date', 'amount', 'created_at']

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user)
        
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category_id=category)
        
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
        
        return queryset

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def financial_summary(request):
    user = request.user
    
    total_income = Income.objects.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0
    total_expense = Expense.objects.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0
    balance = total_income - total_expense
    
    return Response({
        'total_income': float(total_income),
        'total_expense': float(total_expense),
        'balance': float(balance)
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def monthly_report(request):
    user = request.user
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))
    
    start_date = datetime(year, month, 1).date()
    if month == 12:
        end_date = datetime(year + 1, 1, 1).date()
    else:
        end_date = datetime(year, month + 1, 1).date()
    
    monthly_income = Income.objects.filter(
        user=user,
        date__gte=start_date,
        date__lt=end_date
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    monthly_expense = Expense.objects.filter(
        user=user,
        date__gte=start_date,
        date__lt=end_date
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    return Response({
        'year': year,
        'month': month,
        'income': float(monthly_income),
        'expense': float(monthly_expense),
        'net': float(monthly_income - monthly_expense)
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_report(request):
    user = request.user
    
    income_by_category = Income.objects.filter(user=user).values(
        'category__name'
    ).annotate(total=Sum('amount')).order_by('-total')
    
    expense_by_category = Expense.objects.filter(user=user).values(
        'category__name'
    ).annotate(total=Sum('amount')).order_by('-total')
    
    return Response({
        'income_by_category': [
            {'category': item['category__name'], 'total': float(item['total'])}
            for item in income_by_category
        ],
        'expense_by_category': [
            {'category': item['category__name'], 'total': float(item['total'])}
            for item in expense_by_category
        ]
    })

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def dashboard_page(request):
    return render(request, 'dashboard.html')



