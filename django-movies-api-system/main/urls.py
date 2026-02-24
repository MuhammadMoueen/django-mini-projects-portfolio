from django.urls import path
from . import views

urlpatterns = [
    path('api-docs/', views.api_docs, name='api_docs'),
    
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/create/', views.actor_create, name='actor_create'),
    path('actors/edit/<int:actor_id>/', views.actor_edit, name='actor_edit'),
    path('actors/delete/<int:actor_id>/', views.actor_delete, name='actor_delete'),
    
    path('directors/', views.director_list, name='director_list'),
    path('directors/create/', views.director_create, name='director_create'),
    path('directors/edit/<int:director_id>/', views.director_edit, name='director_edit'),
    path('directors/delete/<int:director_id>/', views.director_delete, name='director_delete'),
    
    path('languages/', views.language_list, name='language_list'),
    path('languages/create/', views.language_create, name='language_create'),
    path('languages/edit/<int:language_id>/', views.language_edit, name='language_edit'),
    path('languages/delete/<int:language_id>/', views.language_delete, name='language_delete'),
    
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/create/', views.genre_create, name='genre_create'),
    path('genres/edit/<int:genre_id>/', views.genre_edit, name='genre_edit'),
    path('genres/delete/<int:genre_id>/', views.genre_delete, name='genre_delete'),
    
    path('', views.movie_list, name='movie_list'),
    path('movies/create/', views.movie_create, name='movie_create'),
    path('movies/edit/<int:movie_id>/', views.movie_edit, name='movie_edit'),
    path('movies/delete/<int:movie_id>/', views.movie_delete, name='movie_delete'),
]