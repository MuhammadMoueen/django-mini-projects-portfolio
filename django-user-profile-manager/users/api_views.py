from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def api_profile_completion(request):
    completion = request.user.profile.profile_completion_percentage
    return JsonResponse({'completion': completion})

@login_required
def api_profile_data(request):
    profile = request.user.profile
    data = {
        'username': request.user.username,
        'email': request.user.email,
        'full_name': profile.full_name,
        'bio': profile.bio,
        'phone': profile.phone,
        'location': profile.location,
        'profile_picture': profile.profile_picture.url if profile.profile_picture else None,
        'completion': profile.profile_completion_percentage,
    }
    return JsonResponse(data)
