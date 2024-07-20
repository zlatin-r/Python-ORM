from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from main_app.mixins import AwardedMixin, UpdatedMixin


# Create your models here.

class BasePerson(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(
        max_length=50,
        default='Unknown'
    )

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True


class Director(BasePerson):
    years_of_experience = models.SmallIntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )


class Actor(BasePerson, AwardedMixin, UpdatedMixin):
    pass


class Movie(AwardedMixin, UpdatedMixin):
    class GenreChoices(models.TextChoices):
        ACTION = "Action", "Action"
        COMEDY = "Comedy", "Comedy"
        DRAMA = "Drama", "Drama"
        OTHER = "Other", "Other"

    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)]
    ),
    release_date = models.DateField(),
    storyline = models.TextField(null=True, blank=True),
    genre = models.CharField(
        max_length=6,
        choices=GenreChoices.choices,
        default=GenreChoices.OTHER
    ),
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0),
        ],
        default=0.0
    ),
    is_classic = models.BooleanField(default=False),
    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
        related_name='director_movies'
    ),
    starring_actor = models.ForeignKey(
        to=Actor,
        on_delete=models.SET_NULL,
        related_name='starring_actor_movies',
        null=True,
        blank=True
    ),
    actors = models.ManyToManyField(
        to=Actor,
        related_name='actor_movies'
    )

    def __str__(self):
        return self.title
