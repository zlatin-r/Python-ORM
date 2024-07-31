from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import DirectorManager
from main_app.mixins import PersonInfo, LastUpdated, IsAwarded


# Create your models here.
class Director(PersonInfo):
    years_of_experience = models.SmallIntegerField(validators=[MinValueValidator(0)], default=0)

    objects = DirectorManager()


class Actor(PersonInfo, LastUpdated, IsAwarded):
    is_awarded = models.BooleanField(default=False)


class Movie(IsAwarded, LastUpdated):
    class GenreChoices(models.TextChoices):
        ACTION = "Action", "Action"
        COMEDY = "Comedy", "Comedy"
        DRAMA = "Drama", "Drama"
        OTHER = "Other", "Other"

    title = models.CharField(max_length=150, validators=[MinLengthValidator(5)])
    release_date = models.DateField()
    storyline = models.TextField(null=True, blank=True)
    genre = models.CharField(choices=GenreChoices, max_length=6, default=GenreChoices.OTHER)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0,
                                 validators=[MinValueValidator(0), MaxValueValidator(10)])
    is_classic = models.BooleanField(default=False)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director_movies')
    starring_actor = models.ForeignKey(Actor, on_delete=models.SET_NULL, null=True, related_name='starring_actors')
    actors = models.ManyToManyField(Actor, related_name='actors')
