from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    GenreViewSet, LanguageViewSet, ActorViewSet, 
    DirectorViewSet, MovieViewSet
)

router = DefaultRouter()
router.register(r'genres', GenreViewSet, basename='api-genre')
router.register(r'languages', LanguageViewSet, basename='api-language')
router.register(r'actors', ActorViewSet, basename='api-actor')
router.register(r'directors', DirectorViewSet, basename='api-director')
router.register(r'movies', MovieViewSet, basename='api-movie')

urlpatterns = [
    path('', include(router.urls)),
]
