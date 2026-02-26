from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from rest_framework import serializers
from .models import Category, Income, Expense, UserProfile


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration with password validation.
    """
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField(required=True, validators=[EmailValidator()])

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value.lower()

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user authentication.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user basic information.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for complete user profile with extended fields.
    """
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name', allow_blank=True)
    last_name = serializers.CharField(source='user.last_name', allow_blank=True)
    profile_picture = serializers.SerializerMethodField()
    
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture', 'bio', 'phone']
    
    def get_profile_picture(self, obj):
        if obj.profile_picture:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.profile_picture.url)
        return None
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user
        
        # Update user fields
        if 'email' in user_data:
            user.email = user_data['email']
        if 'first_name' in user_data:
            user.first_name = user_data['first_name']
        if 'last_name' in user_data:
            user.last_name = user_data['last_name']
        user.save()
        
        # Update profile fields
        instance.bio = validated_data.get('bio', instance.bio)
        instance.phone = validated_data.get('phone', instance.phone)
        
        # Handle profile picture from request.FILES
        request = self.context.get('request')
        if request and request.FILES.get('profile_picture'):
            instance.profile_picture = request.FILES['profile_picture']
        
        instance.save()
        
        return instance

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for category management.
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_type', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class IncomeSerializer(serializers.ModelSerializer):
    """
    Serializer for income transactions with validation.
    """
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Income
        fields = ['id', 'amount', 'date', 'notes', 'category', 'category_name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero")
        return value

    def validate_category(self, value):
        if value and value.user != self.context['request'].user:
            raise serializers.ValidationError("Invalid category")
        if value and value.category_type != 'income':
            raise serializers.ValidationError("Category must be of type income")
        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class ExpenseSerializer(serializers.ModelSerializer):
    """
    Serializer for expense transactions with validation.
    """
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'date', 'notes', 'category', 'category_name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero")
        return value

    def validate_category(self, value):
        if value and value.user != self.context['request'].user:
            raise serializers.ValidationError("Invalid category")
        if value and value.category_type != 'expense':
            raise serializers.ValidationError("Category must be of type expense")
        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

