from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import CV, Project, ContactMessage
from .forms import ContactForm

def home(request):
    active_cv = CV.objects.filter(is_active=True).first()
    featured_projects = Project.objects.filter(featured=True)[:3]
    context = {
        'active_cv': active_cv,
        'featured_projects': featured_projects,
    }
    return render(request, 'home.html', context)

def about(request):
    active_cv = CV.objects.filter(is_active=True).first()
    context = {
        'active_cv': active_cv,
    }
    return render(request, 'about.html', context)

def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects,
    }
    return render(request, 'projects.html', context)

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
