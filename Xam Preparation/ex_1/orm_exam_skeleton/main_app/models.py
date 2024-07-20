from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from main_app.mixins import AwardedMixin, UpdatedMixin


# Create your models here.

class Base(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2),
        ]
    )
    birth_date = models.DateField(
        default='1900-01-01'
    )
    nationality = models.CharField(
        max_length=50,
        default='Unknown'
    )


class Director(Base):
    years_of_experience = models.SmallIntegerField(
        validators=[
            MinValueValidator(0),
        ],
        default=0
    )


class Actor(Base, AwardedMixin, UpdatedMixin):
    pass


class Movie(AwardedMixin, UpdatedMixin):
    class GenreChoices(models.TextChoices):
        ACTION = "Action", "Action"
        COMEDY = "Comedy", "Comedy"
        DRAMA = "Drama", "Drama"
        OTHER = "Other", "Other"

    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(5),
        ]
    ),
    release_date = models.DateField(),
    storyline = models.TextField(
        null=True,
        blank=True,
    ),
    genre = models.CharField(
        choices=GenreChoices,
        max_length=6,
        default='Other',
    ),
    rating = models.DecimalField(
        3,
        1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        default=0,
    ),
    is_classic = models.BooleanField(
        default=False,
    ),
    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE
    ),
    starring_actor = models.ForeignKey(
        to=Actor,
        null=True,
        on_delete=models.SET_NULL,
    ),
    actors = models.ManyToManyField(
        to=Actor,
    )
