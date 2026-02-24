from django import forms
from .models import Actor, Director, Genre, Language, Movie


class ActorForm(forms.ModelForm):
    """ModelForm for Actor model."""
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name', 'dob']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),
            'dob': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'dob': 'Date of Birth',
        }


class DirectorForm(forms.ModelForm):
    """ModelForm for Director model."""
    class Meta:
        model = Director
        fields = ['first_name', 'last_name', 'dob']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),
            'dob': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'dob': 'Date of Birth',
        }


class GenreForm(forms.ModelForm):
    """ModelForm for Genre model."""
    class Meta:
        model = Genre
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter genre name'
            }),
        }
        labels = {
            'name': 'Genre Name',
        }


class LanguageForm(forms.ModelForm):
    """ModelForm for Language model."""
    class Meta:
        model = Language
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter language name'
            }),
        }
        labels = {
            'name': 'Language Name',
        }


class MovieForm(forms.ModelForm):
    """ModelForm for Movie model."""
    class Meta:
        model = Movie
        fields = [
            'title', 'description', 'duration', 'release_date', 
            'rating', 'genre', 'language', 'director', 
            'poster_image', 'actors'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter movie title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter movie description'
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duration in minutes'
            }),
            'release_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',
                'placeholder': 'e.g., 8.5'
            }),
            'genre': forms.Select(attrs={
                'class': 'form-control'
            }),
            'language': forms.Select(attrs={
                'class': 'form-control'
            }),
            'director': forms.Select(attrs={
                'class': 'form-control'
            }),
            'poster_image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'actors': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'title': 'Movie Title',
            'description': 'Description',
            'duration': 'Duration (minutes)',
            'release_date': 'Release Date',
            'rating': 'Rating (0-10)',
            'genre': 'Genre',
            'language': 'Language',
            'director': 'Director',
            'poster_image': 'Poster Image',
            'actors': 'Actors',
        }
