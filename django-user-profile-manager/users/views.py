from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import (
    UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CustomPasswordChangeForm,
    PersonalInfoForm, EducationForm, SkillForm, ExperienceForm, ProjectForm
)
from .models import UserProfile, Education, Skill, Experience, Project

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_page = request.GET.get('next', 'dashboard')
            return redirect(next_page)
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'users/login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')

@login_required
def dashboard(request):
    profile = request.user.profile
    context = {
        'profile': profile,
        'completion_percentage': profile.profile_completion_percentage,
        'education_count': profile.education_set.count(),
        'skills_count': profile.skill_set.count(),
        'experience_count': profile.experience_set.count(),
        'projects_count': profile.project_set.count(),
    }
    return render(request, 'users/dashboard.html', context)

@login_required
def profile_view(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user
    profile = user.profile
    return render(request, 'users/profile.html', {'profile': profile, 'user_obj': user})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile_edit.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})

# ===== Personal Information =====
@login_required
def personal_info(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal information updated successfully!')
            return redirect('dashboard')
    else:
        form = PersonalInfoForm(instance=profile)
    return render(request, 'users/personal_info.html', {'form': form, 'profile': profile})

# ===== Education CRUD =====
@login_required
def education_list(request):
    education_items = request.user.profile.education_set.all()
    return render(request, 'users/education_list.html', {'education_items': education_items})

@login_required
def education_add(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.profile = request.user.profile
            education.save()
            messages.success(request, 'Education entry added successfully!')
            return redirect('education_list')
    else:
        form = EducationForm()
    return render(request, 'users/education_form.html', {'form': form, 'title': 'Add Education'})

@login_required
def education_edit(request, pk):
    education = get_object_or_404(Education, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education entry updated successfully!')
            return redirect('education_list')
    else:
        form = EducationForm(instance=education)
    return render(request, 'users/education_form.html', {'form': form, 'title': 'Edit Education'})

@login_required
def education_delete(request, pk):
    education = get_object_or_404(Education, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        education.delete()
        messages.success(request, 'Education entry deleted successfully!')
        return redirect('education_list')
    return render(request, 'users/confirm_delete.html', {'object': education, 'type': 'Education'})

# ===== Skills CRUD =====
@login_required
def skills_list(request):
    skills = request.user.profile.skill_set.all()
    return render(request, 'users/skills_list.html', {'skills': skills})

@login_required
def skill_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.profile = request.user.profile
            skill.save()
            messages.success(request, 'Skill added successfully!')
            return redirect('skills_list')
    else:
        form = SkillForm()
    return render(request, 'users/skill_form.html', {'form': form, 'title': 'Add Skill'})

@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully!')
            return redirect('skills_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'users/skill_form.html', {'form': form, 'title': 'Edit Skill'})

@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully!')
        return redirect('skills_list')
    return render(request, 'users/confirm_delete.html', {'object': skill, 'type': 'Skill'})

# ===== Experience CRUD =====
@login_required
def experience_list(request):
    experiences = request.user.profile.experience_set.all()
    return render(request, 'users/experience_list.html', {'experiences': experiences})

@login_required
def experience_add(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.profile = request.user.profile
            experience.save()
            messages.success(request, 'Experience added successfully!')
            return redirect('experience_list')
    else:
        form = ExperienceForm()
    return render(request, 'users/experience_form.html', {'form': form, 'title': 'Add Experience'})

@login_required
def experience_edit(request, pk):
    experience = get_object_or_404(Experience, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experience updated successfully!')
            return redirect('experience_list')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'users/experience_form.html', {'form': form, 'title': 'Edit Experience'})

@login_required
def experience_delete(request, pk):
    experience = get_object_or_404(Experience, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        experience.delete()
        messages.success(request, 'Experience deleted successfully!')
        return redirect('experience_list')
    return render(request, 'users/confirm_delete.html', {'object': experience, 'type': 'Experience'})

# ===== Projects CRUD =====
@login_required
def projects_list(request):
    projects = request.user.profile.project_set.all()
    return render(request, 'users/projects_list.html', {'projects': projects})

@login_required
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = request.user.profile
            project.save()
            messages.success(request, 'Project added successfully!')
            return redirect('projects_list')
    else:
        form = ProjectForm()
    return render(request, 'users/project_form.html', {'form': form, 'title': 'Add Project'})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('projects_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'users/project_form.html', {'form': form, 'title': 'Edit Project'})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('projects_list')
    return render(request, 'users/confirm_delete.html', {'object': project, 'type': 'Project'})

