from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import CV, Project, ContactMessage
from .forms import ContactForm

def home(request):
    """Display homepage with latest projects and active CV."""
    active_cv = CV.objects.filter(is_active=True).first()
    featured_projects = Project.objects.filter(featured=True).order_by('-order')[:3]
    context = {
        'active_cv': active_cv,
        'featured_projects': featured_projects,
    }
    return render(request, 'home.html', context)

def about(request):
    """Display about page with active CV."""
    active_cv = CV.objects.filter(is_active=True).first()
    context = {
        'active_cv': active_cv,
    }
    return render(request, 'about.html', context)

def projects(request):
    """Display all projects."""
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects,
    }
    return render(request, 'projects.html', context)

def blog(request):
    """Display blog page."""
    return render(request, 'blog.html')

def contact(request):
    """Handle contact form submission and display contact page."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            try:
                subject = f"New Contact Message from {contact_message.name}"
                message = f"""
You have received a new contact message:

Name: {contact_message.name}
Email: {contact_message.email}
Message:
{contact_message.message}

Sent at: {contact_message.created_at.strftime('%Y-%m-%d %H:%M:%S')}
                """
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Thank you! Your message has been sent successfully.'})
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
