from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import Actor, Director, Genre, Language, Movie
from .forms import ActorForm, DirectorForm, GenreForm, LanguageForm, MovieForm


def api_docs(request):
    return render(request, 'api_docs.html')


def actor_list(request):
    return render(request, 'actor_list.html')


def actor_create(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            actor = form.save()
            messages.success(request, f'Actor "{actor.first_name} {actor.last_name}" created successfully!')
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


def actor_edit(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)
    
    if request.method == 'POST':
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            messages.success(request, f'Actor "{actor.first_name} {actor.last_name}" updated successfully!')
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


@require_http_methods(["POST"])
def actor_delete(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)
    actor_name = f"{actor.first_name} {actor.last_name}"
    actor.delete()
    messages.success(request, f'Actor "{actor_name}" deleted successfully!')
    return redirect('actor_list')


def director_list(request):
    return render(request, 'director_list.html')


def director_create(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            director = form.save()
            messages.success(request, f'Director "{director.first_name} {director.last_name}" created successfully!')
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


def director_edit(request, director_id):
    director = get_object_or_404(Director, id=director_id)
    
    if request.method == 'POST':
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            messages.success(request, f'Director "{director.first_name} {director.last_name}" updated successfully!')
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


@require_http_methods(["POST"])
def director_delete(request, director_id):
    director = get_object_or_404(Director, id=director_id)
    director_name = f"{director.first_name} {director.last_name}"
    director.delete()
    messages.success(request, f'Director "{director_name}" deleted successfully!')
    return redirect('director_list')


def language_list(request):
    return render(request, 'language_list.html')


def language_create(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.save()
            messages.success(request, f'Language "{language.name}" created successfully!')
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


def language_edit(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            messages.success(request, f'Language "{language.name}" updated successfully!')
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


@require_http_methods(["POST"])
def language_delete(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    language_name = language.name
    language.delete()
    messages.success(request, f'Language "{language_name}" deleted successfully!')
    return redirect('language_list')


def genre_list(request):
    return render(request, 'genre_list.html')


def genre_create(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save()
            messages.success(request, f'Genre "{genre.name}" created successfully!')
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


def genre_edit(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            messages.success(request, f'Genre "{genre.name}" updated successfully!')
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


@require_http_methods(["POST"])
def genre_delete(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    genre_name = genre.name
    genre.delete()
    messages.success(request, f'Genre "{genre_name}" deleted successfully!')
    return redirect('genre_list')


def movie_list(request):
    return render(request, 'movie_list.html')


def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            messages.success(request, f'Movie "{movie.title}" created successfully!')
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


def movie_edit(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, f'Movie "{movie.title}" updated successfully!')
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


@require_http_methods(["POST"])
def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie_title = movie.title
    movie.delete()
    messages.success(request, f'Movie "{movie_title}" deleted successfully!')
    return redirect('movie_list')
