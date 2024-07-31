import os
import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Actor, Movie, Director


# Create queries within functions

def get_directors(search_name=None, search_nationality=None):
    query = None

    if search_name and search_nationality:
        query = Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality)
    elif search_name and not search_nationality:
        query = Q(full_name__icontains=search_name)
    elif not search_name and search_nationality:
        query = Q(nationality__icontains=search_nationality)
    else:
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


def get_actors_by_movies_count():
    actors = Actor.objects.annotate(count_movies=Count("actors")) \
                 .order_by("-count_movies", "full_name")[:3]

    if not actors or actors[0].count_movies == 0:
        return ""

    result = [f"{a.full_name}, participated in {a.count_movies} movies" for a in actors]

    return "\n".join(result)


def get_top_rated_awarded_movie():
    movie = Movie.objects.all().filter(is_awarded=True).order_by("-rating", "title").first()

    if not movie:
        return ""

    starring_actor = movie.starring_actor.full_name if movie.starring_actor else "N/A"
    cast = [a.full_name for a in movie.actors.all().order_by("full_name")]

    return f"Top rated awarded movie: {movie.title}, " \
           f"rating: {movie.rating}. " \
           f"Starring actor: {starring_actor}. " \
           f"Cast: {', '.join(cast)}."


def increase_rating():
    movies = Movie.objects.filter(is_classic=True, rating__lt=10)

    if not movies:
        return "No ratings increased."

    movies.update(rating=F("rating") + 0.1)

    return f"Rating increased for {movies.count()} movies."
