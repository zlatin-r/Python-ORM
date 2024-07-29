import os
import django
from django.db.models import Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


# Create queries within functions

def get_directors(search_name=None, search_nationality=None):
    directors = None

    if not search_name and not search_nationality:
        return ""
    elif search_name and search_nationality:
        directors = Director.objects.filter(full_name__icontains=search_name,
                                            nationality__icontains=search_nationality)
    elif search_name and not search_nationality:
        directors = Director.objects.filter(full_name__icontains=search_name)
    elif not search_name and search_nationality:
        directors = Director.objects.filter(nationality__icontains=search_nationality)

    if not directors:
        return ""

    result = [f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}"
              for d in directors]

    return "\n".join(result) if result else ""


def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count()

    if not top_director:
        return ""

    return f"Top Director: {top_director.full_name}, movies: {top_director.count_movies}."


def get_top_actor():
    top_actor = Actor.objects.prefetch_related("starring_act_movies") \
        .annotate(count_movies=Count("starring_act_movies"),
                  avg_rating=Avg("starring_act_movies__rating")) \
        .order_by("-count_movies", "full_name") \
        .first()

    if not top_actor or not top_actor.count_movies:
        return ""

    staring_movies = ", ".join(m.title for m in top_actor.starring_act_movies.all() if m)

    return (f"Top Actor: {top_actor.full_name}, "
            f"starring in movies: {staring_movies}, "
            f"movies average rating: {top_actor.avg_rating:.1f}")



