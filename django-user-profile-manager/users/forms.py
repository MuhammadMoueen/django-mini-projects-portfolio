from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].help_text = 'Required. 150 characters or fewer.'
        self.fields['email'].help_text = 'Enter a valid email address.'

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'full_name', 'bio', 'phone', 'location']
        labels = {
            'profile_picture': 'Profile Picture',
            'full_name': 'Full Name',
            'bio': 'About Me',
            'phone': 'Phone Number',
            'location': 'City/Location',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'profile_picture':
                self.fields[field].widget.attrs.update({'class': 'form-control-file'})
            elif field == 'bio':
                self.fields[field].widget.attrs.update({'class': 'form-control', 'rows': 4})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        self.fields['full_name'].widget.attrs['placeholder'] = 'Enter your full name'
        self.fields['bio'].widget.attrs['placeholder'] = 'Tell us about yourself...'
        self.fields['phone'].widget.attrs['placeholder'] = '+1 234 567 8900'
        self.fields['location'].widget.attrs['placeholder'] = 'City, Country'

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
