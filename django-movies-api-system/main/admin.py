from django.contrib import admin

from .models import Genre, Language, Actor, Director, Movie

# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob')
    search_fields = ('first_name', 'last_name')
    list_filter = ('dob',)
    date_hierarchy = 'dob'
    # filter_horizontal

admin.site.register(Actor, ActorAdmin)



class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob')
    search_fields = ('first_name', 'last_name')
    list_filter = ('dob',)
admin.site.register(Director, DirectorAdmin)



class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Genre, GenreAdmin)



class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Language, LanguageAdmin)



class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration', 'genre', 'language', 'director', 'rating', 'get_actors')
    def get_actors(self, obj):
        actors = obj.actors.all()
        a = []
        for actor in actors:
            a.append(actor.first_name + actor.last_name)
        return a
    search_fields = ('title', 'description')
    list_filter = ('release_date', 'genre', 'language', 'director')
    date_hierarchy = 'release_date'
    filter_horizontal = ('actors',)
admin.site.register(Movie, MovieAdmin)