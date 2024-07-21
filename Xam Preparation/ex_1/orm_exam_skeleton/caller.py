import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Director, Actor


# Create queries within functions

def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    query_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)

    if search_name is not None and search_nationality is not None:
        query = Q(query_name & query_nationality)
    elif search_name is not None:
        query = query_name
    else:
        query = query_nationality

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ""

    result = []

    for d in directors:
        result.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")

    return "\n".join(result)


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ""

    return f"Top Director: {director.full_name}, movies: {director.movies_count}"


def get_top_actor():
    actor = Actor.objects.prefetch_related("starring_movies").annotate(
        movie_count=Count("starring_movies"),
        avg_rating=Avg("starring_movies__rating")
    ).order_by("-movie_count", "full_name").first()

