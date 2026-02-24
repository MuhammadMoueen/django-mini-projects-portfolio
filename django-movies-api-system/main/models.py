from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField()  # minutes
    release_date = models.DateField()
    # single foreign-key genre (original behavior)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='movies')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, related_name= 'movies')
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    poster_image = models.ImageField(upload_to='posters/', null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name= 'movies')

    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.title