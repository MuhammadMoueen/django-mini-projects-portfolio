from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import UserProfile, Education, Skill, Experience, Project

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        self.fields['username'].widget.attrs['placeholder'] = 'Choose a username'
        self.fields['email'].widget.attrs['placeholder'] = 'your.email@example.com'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create a strong password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

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

class PersonalInfoForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )
    
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'full_name', 'father_name', 'date_of_birth', 'phone', 'address']
        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your father's name"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1 234 567 8900'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your complete address'}),
        }

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

class EducationForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )
    
    class Meta:
        model = Education
        fields = ['university_name', 'degree', 'cgpa', 'start_date', 'end_date', 'description']
        widgets = {
            'university_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'University Name'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bachelor of Science in Computer Science'}),
            'cgpa': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '3.5', 'step': '0.01', 'min': '0', 'max': '4'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe your education details...'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name', 'level', 'certificate_file', 'certificate_link']
        widgets = {
            'skill_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Python, Django, React'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'certificate_file': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpg,.png'}),
            'certificate_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://certificate-url.com'}),
        }

class ExperienceForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=True
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )
    
    class Meta:
        model = Experience
        fields = ['job_title', 'company_name', 'start_date', 'end_date', 'is_current', 'description']
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Software Engineer'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'is_current': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe your role and responsibilities...'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'skills_used', 'live_link', 'github_link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe your project...'}),
            'skills_used': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python, Django, PostgreSQL, Docker'}),
            'live_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://live-demo.com'}),
            'github_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/username/repo'}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
