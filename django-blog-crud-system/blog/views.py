from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime, timedelta
from .models import Post
from .forms import UserRegisterForm, PostForm, UserUpdateForm, ProfileUpdateForm, CustomPasswordChangeForm

def home(request):
    """
    Display the home page with all blog posts.
    
    Features:
    - Search functionality (title, content, author)
    - Sorting options (newest, oldest, by title)
    - Pagination (6 posts per page)
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered home page with posts and pagination
    """
    posts = Post.objects.all()
    
    search_query = request.GET.get('search', '')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(author__username__icontains=search_query)
        )
    
    sort_by = request.GET.get('sort', 'newest')
    if sort_by == 'oldest':
        posts = posts.order_by('created_at')
    elif sort_by == 'title':
        posts = posts.order_by('title')
    else:
        posts = posts.order_by('-created_at')
    
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    
    return render(request, 'blog/home.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {user.username}!')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    
    return render(request, 'blog/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'blog/login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def dashboard(request):
    user_posts = Post.objects.filter(author=request.user)
    total_posts = user_posts.count()
    
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)
    posts_this_week = user_posts.filter(created_at__date__gte=week_ago).count()
    
    recent_posts = user_posts[:5]
    
    context = {
        'posts': user_posts,
        'total_posts': total_posts,
        'posts_this_week': posts_this_week,
        'recent_posts': recent_posts,
    }
    
    return render(request, 'blog/dashboard.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Create'})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user and not request.user.is_superuser:
        messages.error(request, 'You can only edit your own posts.')
        return redirect('post_detail', pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Edit', 'post': post})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user and not request.user.is_superuser:
        messages.error(request, 'You can only delete your own posts.')
        return redirect('post_detail', pk=pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('dashboard')
    
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def author_posts(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author)
    
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'author': author,
        'page_obj': page_obj,
        'total_posts': posts.count(),
    }
    
    return render(request, 'blog/author_posts.html', context)

@login_required
def edit_profile(request):
    """
    Edit user profile page with user info and profile picture upload.
    
    Features:
    - Update first name, last name, email
    - Upload profile picture with preview
    - Update bio
    - Username is read-only
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered edit profile page with forms
    """
    if request.method == 'POST':
        # Process both user and profile forms
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('dashboard')
    else:
        # Initialize forms with current data
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    
    return render(request, 'blog/edit_profile.html', context)

@login_required
def change_password(request):
    """
    Change user password page with validation.
    
    Features:
    - Verify old password
    - Set new password with confirmation
    - Password strength validation
    - Session preserved after password change
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered change password page
    """
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Keep user logged in after password change
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('change_password')
    else:
        form = CustomPasswordChangeForm(request.user)
    
    return render(request, 'blog/change_password.html', {'form': form})
