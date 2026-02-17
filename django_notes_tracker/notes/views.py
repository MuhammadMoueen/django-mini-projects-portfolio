from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Note


def home(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        notes = Note.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).order_by('created_at')
    else:
        notes = Note.objects.all().order_by('created_at')
    
    total_notes = Note.objects.count()
    
    context = {
        'notes': notes,
        'total_notes': total_notes,
        'search_query': search_query,
    }
    
    return render(request, 'notes/home.html', context)


def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        
        if not title:
            messages.error(request, 'Title is required!')
            return render(request, 'notes/add_note.html', {'content': content})
        
        if not content:
            messages.error(request, 'Content is required!')
            return render(request, 'notes/add_note.html', {'title': title})
        
        note = Note.objects.create(title=title, content=content)
        messages.success(request, f'Note "{note.title}" has been created successfully!')
        return redirect('home')
    
    return render(request, 'notes/add_note.html')


def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    context = {'note': note}
    return render(request, 'notes/view_note.html', context)


def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        
        if not title:
            messages.error(request, 'Title is required!')
            return render(request, 'notes/edit_note.html', {'note': note, 'content': content})
        
        if not content:
            messages.error(request, 'Content is required!')
            return render(request, 'notes/edit_note.html', {'note': note, 'title': title})
        
        note.title = title
        note.content = content
        note.save()
        messages.success(request, f'Note "{note.title}" has been updated successfully!')
        return redirect('view_note', note_id=note.id)
    
    context = {'note': note}
    return render(request, 'notes/edit_note.html', context)


def delete_note(request, note_id):
    if request.method == 'POST':
        note = get_object_or_404(Note, id=note_id)
        note_title = note.title
        note.delete()
        messages.success(request, f'Note "{note_title}" has been deleted successfully!')
    
    return redirect('home')
