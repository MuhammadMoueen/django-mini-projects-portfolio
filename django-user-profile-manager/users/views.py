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
    
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        messages.success(request, f'Account created for {user.username}! You can now login.')
        return redirect('login')
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect(request.GET.get('next', 'dashboard'))
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
    return render(request, 'users/dashboard.html', {
        'profile': profile,
        'completion_percentage': profile.profile_completion_percentage,
        'education_count': profile.education_set.count(),
        'skills_count': profile.skill_set.count(),
        'experience_count': profile.experience_set.count(),
        'projects_count': profile.project_set.count(),
    })


@login_required
def profile_view(request, username=None):
    user = get_object_or_404(User, username=username) if username else request.user
    return render(request, 'users/profile.html', {
        'profile': user.profile,
        'user_obj': user
    })


@login_required
def profile_edit(request):
    user_form = UserUpdateForm(request.POST or None, instance=request.user)
    profile_form = ProfileUpdateForm(
        request.POST or None,
        request.FILES or None,
        instance=request.user.profile
    )
    
    if request.method == 'POST' and user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        messages.success(request, 'Your profile has been updated successfully!')
        return redirect('profile')
    
    return render(request, 'users/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def change_password(request):
    form = CustomPasswordChangeForm(request.user, request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Your password was successfully updated!')
        return redirect('dashboard')
    elif request.method == 'POST':
        messages.error(request, 'Please correct the errors below.')
    return render(request, 'users/change_password.html', {'form': form})


@login_required
def personal_info(request):
    profile = request.user.profile
    form = PersonalInfoForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Personal information updated successfully!')
        return redirect('dashboard')
    return render(request, 'users/personal_info.html', {'form': form, 'profile': profile})


@login_required
def education_list(request):
    return render(request, 'users/education_list.html', {
        'education_items': request.user.profile.education_set.all()
    })


@login_required
def education_add(request):
    form = EducationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        education = form.save(commit=False)
        education.profile = request.user.profile
        education.save()
        messages.success(request, 'Education entry added successfully!')
        return redirect('education_list')
    return render(request, 'users/education_form.html', {'form': form, 'title': 'Add Education'})


@login_required
def education_edit(request, pk):
    education = get_object_or_404(Education, pk=pk, profile=request.user.profile)
    form = EducationForm(request.POST or None, instance=education)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Education entry updated successfully!')
        return redirect('education_list')
    return render(request, 'users/education_form.html', {'form': form, 'title': 'Edit Education'})


@login_required
def education_delete(request, pk):
    education = get_object_or_404(Education, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        education.delete()
        messages.success(request, 'Education entry deleted successfully!')
        return redirect('education_list')
    return render(request, 'users/confirm_delete.html', {'object': education, 'type': 'Education'})


@login_required
def skills_list(request):
    return render(request, 'users/skills_list.html', {
        'skills': request.user.profile.skill_set.all()
    })


@login_required
def skill_add(request):
    form = SkillForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        skill = form.save(commit=False)
        skill.profile = request.user.profile
        skill.save()
        messages.success(request, 'Skill added successfully!')
        return redirect('skills_list')
    return render(request, 'users/skill_form.html', {'form': form, 'title': 'Add Skill'})


@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk, profile=request.user.profile)
    form = SkillForm(request.POST or None, request.FILES or None, instance=skill)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Skill updated successfully!')
        return redirect('skills_list')
    return render(request, 'users/skill_form.html', {'form': form, 'title': 'Edit Skill'})


@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully!')
        return redirect('skills_list')
    return render(request, 'users/confirm_delete.html', {'object': skill, 'type': 'Skill'})


@login_required
def experience_list(request):
    return render(request, 'users/experience_list.html', {
        'experiences': request.user.profile.experience_set.all()
    })


@login_required
def experience_add(request):
    form = ExperienceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        experience = form.save(commit=False)
        experience.profile = request.user.profile
        experience.save()
        messages.success(request, 'Experience added successfully!')
        return redirect('experience_list')
    return render(request, 'users/experience_form.html', {'form': form, 'title': 'Add Experience'})


@login_required
def experience_edit(request, pk):
    experience = get_object_or_404(Experience, pk=pk, profile=request.user.profile)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Experience updated successfully!')
        return redirect('experience_list')
    return render(request, 'users/experience_form.html', {'form': form, 'title': 'Edit Experience'})


@login_required
def experience_delete(request, pk):
    experience = get_object_or_404(Experience, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        experience.delete()
        messages.success(request, 'Experience deleted successfully!')
        return redirect('experience_list')
    return render(request, 'users/confirm_delete.html', {'object': experience, 'type': 'Experience'})


@login_required
def projects_list(request):
    return render(request, 'users/projects_list.html', {
        'projects': request.user.profile.project_set.all()
    })


@login_required
def project_add(request):
    form = ProjectForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        project = form.save(commit=False)
        project.profile = request.user.profile
        project.save()
        messages.success(request, 'Project added successfully!')
        return redirect('projects_list')
    return render(request, 'users/project_form.html', {'form': form, 'title': 'Add Project'})


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk, profile=request.user.profile)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Project updated successfully!')
        return redirect('projects_list')
    return render(request, 'users/project_form.html', {'form': form, 'title': 'Edit Project'})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('projects_list')
    return render(request, 'users/confirm_delete.html', {'object': project, 'type': 'Project'})
