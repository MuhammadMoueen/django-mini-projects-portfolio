from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse

from .models import Actor, Director, Genre, Language, Movie
from .forms import ActorForm, DirectorForm, GenreForm, LanguageForm, MovieForm

# Create your views here.
# Create Actor Views:

# Create Actor List View
def actor_list(request):
    actors = Actor.objects.all()
    context = {'actors': actors}
    return render(request, 'actor_list.html', context)


# Create Actor View:
def actor_create(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actor_list')
    else:
        form = ActorForm()
    
    context = {
        'form': form,
        'title': 'Add New Actor',
        'subtitle': 'Create a new actor profile',
        'icon': 'fas fa-user-plus',
        'submit_text': 'Create Actor',
        'cancel_url': reverse('actor_list')
    }
    return render(request, 'model_form.html', context)


# Create Actor Delete View:
def actor_delete(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)
    actor.delete()
    return redirect('actor_list')    
    

# Create Actor Edit View:
def actor_edit(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)
    
    if request.method == 'POST':
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect('actor_list')
    else:
        form = ActorForm(instance=actor)
    
    context = {
        'form': form,
        'title': 'Edit Actor',
        'subtitle': f'Update details for {actor.first_name} {actor.last_name}',
        'icon': 'fas fa-user-edit',
        'submit_text': 'Update Actor',
        'cancel_url': reverse('actor_list')
    }
    return render(request, 'model_form.html', context)


# Director Views:

# Director List View
def director_list(request):
    directors = Director.objects.all()
    context = {'directors': directors}
    return render(request, 'director_list.html', context)


# Director Create View
def director_create(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('director_list')
    else:
        form = DirectorForm()
    
    context = {
        'form': form,
        'title': 'Add New Director',
        'subtitle': 'Create a new director profile',
        'icon': 'fas fa-person-chalkboard',
        'submit_text': 'Create Director',
        'cancel_url': reverse('director_list')
    }
    return render(request, 'model_form.html', context)


# Director Edit View
def director_edit(request, director_id):
    director = get_object_or_404(Director, id=director_id)
    
    if request.method == 'POST':
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            return redirect('director_list')
    else:
        form = DirectorForm(instance=director)
    
    context = {
        'form': form,
        'title': 'Edit Director',
        'subtitle': f'Update details for {director.first_name} {director.last_name}',
        'icon': 'fas fa-person-chalkboard',
        'submit_text': 'Update Director',
        'cancel_url': reverse('director_list')
    }
    return render(request, 'model_form.html', context)


# Director Delete View
def director_delete(request, director_id):
    director = get_object_or_404(Director, id=director_id)
    director.delete()
    return redirect('director_list')


# Language Views:

# Language List View
def language_list(request):
    languages = Language.objects.all()
    context = {'languages': languages}
    return render(request, 'language_list.html', context)


# Language Create View
def language_create(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('language_list')
    else:
        form = LanguageForm()
    
    context = {
        'form': form,
        'title': 'Add New Language',
        'subtitle': 'Create a new language entry',
        'icon': 'fas fa-language',
        'submit_text': 'Create Language',
        'cancel_url': reverse('language_list')
    }
    return render(request, 'model_form.html', context)


# Language Edit View
def language_edit(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return redirect('language_list')
    else:
        form = LanguageForm(instance=language)
    
    context = {
        'form': form,
        'title': 'Edit Language',
        'subtitle': f'Update details for {language.name}',
        'icon': 'fas fa-language',
        'submit_text': 'Update Language',
        'cancel_url': reverse('language_list')
    }
    return render(request, 'model_form.html', context)


# Language Delete View
def language_delete(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    language.delete()
    return redirect('language_list')


# Genre Views:

# Genre List View
def genre_list(request):
    genres = Genre.objects.all()
    context = {'genres': genres}
    return render(request, 'genre_list.html', context)


# Genre Create View
def genre_create(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm()
    
    context = {
        'form': form,
        'title': 'Add New Genre',
        'subtitle': 'Create a new genre entry',
        'icon': 'fas fa-tag',
        'submit_text': 'Create Genre',
        'cancel_url': reverse('genre_list')
    }
    return render(request, 'model_form.html', context)


# Genre Edit View
def genre_edit(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm(instance=genre)
    
    context = {
        'form': form,
        'title': 'Edit Genre',
        'subtitle': f'Update details for {genre.name}',
        'icon': 'fas fa-tag',
        'submit_text': 'Update Genre',
        'cancel_url': reverse('genre_list')
    }
    return render(request, 'model_form.html', context)


# Genre Delete View
def genre_delete(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    return redirect('genre_list')


# Movie Views:

# Movie List View
def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movie_list.html', context)


# Movie Create View
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    
    context = {
        'form': form,
        'title': 'Add New Movie',
        'subtitle': 'Create a new movie entry',
        'icon': 'fas fa-film',
        'submit_text': 'Create Movie',
        'cancel_url': reverse('movie_list')
    }
    return render(request, 'model_form.html', context)


# Movie Edit View
def movie_edit(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    
    context = {
        'form': form,
        'title': 'Edit Movie',
        'subtitle': f'Update details for {movie.title}',
        'icon': 'fas fa-film',
        'submit_text': 'Update Movie',
        'cancel_url': reverse('movie_list')
    }
    return render(request, 'model_form.html', context)


# Movie Delete View
def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movie_list')