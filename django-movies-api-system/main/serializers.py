from rest_framework import serializers
from django.utils import timezone
from .models import Genre, Language, Actor, Director, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
    
    def validate_name(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Genre name cannot be empty.")
        if len(value) > 100:
            raise serializers.ValidationError("Genre name cannot exceed 100 characters.")
        if Genre.objects.filter(name__iexact=value).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError("A genre with this name already exists.")
        return value.strip()


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']
    
    def validate_name(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Language name cannot be empty.")
        if len(value) > 100:
            raise serializers.ValidationError("Language name cannot exceed 100 characters.")
        if Language.objects.filter(name__iexact=value).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError("A language with this name already exists.")
        return value.strip()


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'dob']
    
    def validate_first_name(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("First name cannot be empty.")
        if len(value) > 100:
            raise serializers.ValidationError("First name cannot exceed 100 characters.")
        return value.strip()
    
    def validate_last_name(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Last name cannot be empty.")
        if len(value) > 100:
            raise serializers.ValidationError("Last name cannot exceed 100 characters.")
        return value.strip()
    
    def validate_dob(self, value):
        if value and value >= timezone.now().date():
            raise serializers.ValidationError("Date of birth must be in the past.")
        return value


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'first_name', 'last_name', 'dob']
    
    def validate_first_name(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("First name cannot be empty.")
        if len(value) > 100:
            raise serializers.ValidationError("First name cannot exceed 100 characters.")
        return value.strip()
    
    def validate_last_name(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Last name cannot be empty.")
        if len(value) > 100:
            raise serializers.ValidationError("Last name cannot exceed 100 characters.")
        return value.strip()
    
    def validate_dob(self, value):
        if value and value >= timezone.now().date():
            raise serializers.ValidationError("Date of birth must be in the past.")
        return value


class MovieSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.name', read_only=True)
    language_name = serializers.CharField(source='language.name', read_only=True)
    director_name = serializers.SerializerMethodField()
    actors_list = ActorSerializer(source='actors', many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'release_date', 
                  'genre', 'genre_name', 'language', 'language_name', 
                  'director', 'director_name', 'poster_image', 'actors', 
                  'actors_list', 'rating']
    
    def get_director_name(self, obj):
        if obj.director:
            return f"{obj.director.first_name} {obj.director.last_name}"
        return None
    
    def validate_title(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Title cannot be empty.")
        if len(value) > 200:
            raise serializers.ValidationError("Title cannot exceed 200 characters.")
        return value.strip()
    
    def validate_duration(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Duration must be a positive number.")
        if value is not None and value > 1000:
            raise serializers.ValidationError("Duration seems unrealistic. Please check the value.")
        return value
    
    def validate_release_date(self, value):
        if value and value > timezone.now().date():
            raise serializers.ValidationError("Release date cannot be in the future.")
        return value
    
    def validate_rating(self, value):
        if value is not None:
            if value < 0 or value > 10:
                raise serializers.ValidationError("Rating must be between 0 and 10.")
        return value
    
    def validate(self, data):
        if 'genre' in data and not data.get('genre'):
            raise serializers.ValidationError({"genre": "Genre is required."})
        if 'language' in data and not data.get('language'):
            raise serializers.ValidationError({"language": "Language is required."})
        return data


class MovieListSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.name', read_only=True)
    language_name = serializers.CharField(source='language.name', read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'release_date', 
                  'genre_name', 'language_name', 'poster_image', 'rating']
