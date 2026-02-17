from django.urls import path
from . import views

urlpatterns = [
    # Home page - displays all notes
    path('', views.home, name='home'),
    
    # Add a new note
    path('add/', views.add_note, name='add_note'),
    
    # View a single note in detail
    path('note/<int:note_id>/', views.view_note, name='view_note'),
    
    # Delete a note
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]
