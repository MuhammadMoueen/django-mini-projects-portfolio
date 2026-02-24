import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies.settings')
django.setup()

from main.models import Genre, Language, Actor, Director, Movie
from datetime import date

print("Clearing existing data...")
Movie.objects.all().delete()
Actor.objects.all().delete()
Director.objects.all().delete()
Language.objects.all().delete()
Genre.objects.all().delete()

print("Creating Genres...")
action = Genre.objects.create(name="Action")
drama = Genre.objects.create(name="Drama")
scifi = Genre.objects.create(name="Sci-Fi")
thriller = Genre.objects.create(name="Thriller")
comedy = Genre.objects.create(name="Comedy")

print("Creating Languages...")
english = Language.objects.create(name="English")
spanish = Language.objects.create(name="Spanish")
french = Language.objects.create(name="French")

print("Creating Directors...")
nolan = Director.objects.create(first_name="Christopher", last_name="Nolan", dob=date(1970, 7, 30))
tarantino = Director.objects.create(first_name="Quentin", last_name="Tarantino", dob=date(1963, 3, 27))
spielberg = Director.objects.create(first_name="Steven", last_name="Spielberg", dob=date(1946, 12, 18))

print("Creating Actors...")
dicaprio = Actor.objects.create(first_name="Leonardo", last_name="DiCaprio", dob=date(1974, 11, 11))
bale = Actor.objects.create(first_name="Christian", last_name="Bale", dob=date(1974, 1, 30))
hardy = Actor.objects.create(first_name="Tom", last_name="Hardy", dob=date(1977, 9, 15))
travolta = Actor.objects.create(first_name="John", last_name="Travolta", dob=date(1954, 2, 18))
jackson = Actor.objects.create(first_name="Samuel L.", last_name="Jackson", dob=date(1948, 12, 21))

print("Creating Movies...")
inception = Movie.objects.create(
    title="Inception",
    description="A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
    duration=148,
    release_date=date(2010, 7, 16),
    rating=8.8,
    genre=scifi,
    language=english,
    director=nolan
)
inception.actors.add(dicaprio, hardy)

dark_knight = Movie.objects.create(
    title="The Dark Knight",
    description="When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
    duration=152,
    release_date=date(2008, 7, 18),
    rating=9.0,
    genre=action,
    language=english,
    director=nolan
)
dark_knight.actors.add(bale, hardy)

pulp_fiction = Movie.objects.create(
    title="Pulp Fiction",
    description="The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.",
    duration=154,
    release_date=date(1994, 10, 14),
    rating=8.9,
    genre=thriller,
    language=english,
    director=tarantino
)
pulp_fiction.actors.add(travolta, jackson)

print("\nSample data created successfully!")
print(f"- {Genre.objects.count()} Genres")
print(f"- {Language.objects.count()} Languages")
print(f"- {Director.objects.count()} Directors")
print(f"- {Actor.objects.count()} Actors")
print(f"- {Movie.objects.count()} Movies")
