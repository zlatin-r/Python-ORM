import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Actor, Movie, Director


# Create queries within functions

def get_directors(search_name=None, search_nationality=None):
    query = None

    if search_name and search_nationality:
        query = Q(full_name__icontains=search_name) | Q(nationality__icontains=search_nationality)
    elif search_name and not search_nationality:
        query = Q(full_name__icontains=search_name)
    elif not search_name and search_nationality:
        query = Q(nationality__icontains=search_nationality)
    elif not search_name and not search_nationality:
        return ""

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ""

    result = [f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}"
              for d in directors]

    return "\n".join(result)


def get_top_director():
    director = Director.objects.annotate(count_movies=Count("director_movies")) \
        .order_by("-count_movies", "full_name") \
        .first()

    if not director or director.count_movies == 0:
        return ""

    return f"Top Director: {director.full_name}, movies: {director.count_movies}."


def get_top_actor():
    actor = Actor.objects.prefetch_related("starring_actors") \
        .annotate(count_st_movies=Count("starring_actors")) \
        .order_by("-count_st_movies", "full_name") \
        .first()

    if not actor or actor.count_st_movies == 0:
        return ""

    starring_movies = ", ".join([m.title for m in actor.starring_actors.all()])
    avg_rating = sum([m.rating for m in actor.starring_actors.all()]) / len(actor.starring_actors.all())

    return (f"Top Actor: {actor.full_name}, "
            f"starring in movies: {starring_movies}, "
            f"movies average rating: {avg_rating:.1f}")
