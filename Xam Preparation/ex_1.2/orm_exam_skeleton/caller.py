import os
import django
from django.db.models import Count, Avg, F

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
              for d in directors.order_by("full_name")]

    return "\n".join(result) if result else ""


def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()

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


def get_actors_by_movies_count():
    actors = Actor.objects.annotate(count_movies=Count("actor_movies")).order_by("-count_movies", "full_name")[:3]

    if not actors or not actors[0].count_movies:
        return ""

    result = [f"{a.full_name}, participated in {a.count_movies} movies" for a in actors]

    return "\n".join(result)


def get_top_rated_awarded_movie():
    movie = Movie.objects.select_related("starring_actor") \
        .prefetch_related("actors") \
        .filter(is_awarded=True) \
        .order_by("-rating", "title") \
        .first()

    if not movie:
        return ""

    starring_actor = movie.starring_actor.full_name if movie.starring_actor else "N/A"
    cast = ", ".join(movie.actors.order_by("full_name").values_list("full_name", flat=True))

    return (f"Top rated awarded movie: {movie.title}, "
            f"rating: {movie.rating}. "
            f"Starring actor: {starring_actor}. "
            f"Cast: {cast}.")


def increase_rating():
    movies = Movie.objects.filter(is_classic=True, rating__lt=10)

    if not movies:
        return "No ratings increased."

    count_movies = movies.count()
    movies.update(rating=F("rating") + 0.1)

    return f"Rating increased for {count_movies} movies."
