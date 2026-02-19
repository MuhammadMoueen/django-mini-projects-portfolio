from django.contrib import messages
from functools import wraps
from django.shortcuts import redirect

def anonymous_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You are already logged in.')
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def profile_completion_required(min_percentage=50):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'profile'):
                completion = request.user.profile.profile_completion_percentage
                if completion < min_percentage:
                    messages.warning(request, f'Please complete your profile to at least {min_percentage}%')
                    return redirect('profile_edit')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
