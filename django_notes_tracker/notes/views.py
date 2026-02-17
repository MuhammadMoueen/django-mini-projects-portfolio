from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Note


def home(request):
    # Get search query if exists
    search_query = request.GET.get('search', '')
    
    if search_query:
        # Filter notes by title or content containing the search query
        notes = Note.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    else:
        # Get all notes, ordered by most recent first
        notes = Note.objects.all()
    
    # Get total count of notes
    total_notes = Note.objects.count()
    
    context = {
        'notes': notes,
        'total_notes': total_notes,
        'search_query': search_query,
    }
    
    return render(request, 'notes/home.html', context)


def add_note(request):
    """
    Handle the creation of a new note.
    
    GET: Display the form to create a new note
    POST: Process the form submission and create a new note
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered form page or redirect to home
    """
    if request.method == 'POST':
        # Get form data from POST request
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        
        # Validate form data
        if not title:
            messages.error(request, 'Title is required!')
            return render(request, 'notes/add_note.html', {
                'content': content
            })
        
        if not content:
            messages.error(request, 'Content is required!')
            return render(request, 'notes/add_note.html', {
                'title': title
            })
        
        # Create new note using Django ORM
        note = Note.objects.create(
            title=title,
            content=content
        )
        
        # Display success message
        messages.success(request, f'Note "{note.title}" has been created successfully!')
        
        # Redirect to home page
        return redirect('home')
    
    # Display the add note form for GET request
    return render(request, 'notes/add_note.html')


def view_note(request, note_id):
    """
    Display a single note in detail.
    
    Args:
        request: HttpRequest object
        note_id (int): ID of the note to display
        
    Returns:
        HttpResponse: Rendered note detail page
    """
    # Get the note or return 404 if not found
    note = get_object_or_404(Note, id=note_id)
    
    context = {
        'note': note,
    }
    
    return render(request, 'notes/view_note.html', context)


def delete_note(request, note_id):
    """
    Handle the deletion of a note.
    
    Only accepts POST requests for security reasons (prevents accidental deletion via GET).
    
    Args:
        request: HttpRequest object
        note_id (int): ID of the note to delete
        
    Returns:
        HttpResponse: Redirect to home page
    """
    if request.method == 'POST':
        # Get the note or return 404 if not found
        note = get_object_or_404(Note, id=note_id)
        
        # Store title for success message
        note_title = note.title
        
        # Delete the note using Django ORM
        note.delete()
        
        # Display success message
        messages.success(request, f'Note "{note_title}" has been deleted successfully!')
    
    # Redirect to home page
    return redirect('home')
