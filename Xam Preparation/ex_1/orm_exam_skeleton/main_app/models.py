from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Director(models.Model):
    full_name = models.CharField(
        validators=[
            MaxLengthValidator(120),
            MinLengthValidator(2)
        ]
    )
    birth_date = models.DateField(
        default="1900-01-01"
    )
    nationality = models.CharField(
        validators=[
            MaxLengthValidator(50)
        ],
        default="Unknown"
    )
    years_of_experience = models.SmallIntegerField(
        validators=[
            MinValueValidator(0),
        ],
        default=0
    )


class Actor(models.Model):
    full_name = models.CharField(
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(120)
        ]
    )
    birth_date = models.DateField(
        default="1900-01-01"
    )
    nationality = models.CharField(
        validators=[
            MaxLengthValidator(50)
        ],
        default="Unknown"
    )
    is_awarded = models.BooleanField(
        default=False
    )
    last_updated = models.DateField(
        auto_now=True
    )


class Movie(models.Model):
    class GenreChoices(models.TextChoices):
        ACTION = 'Action', 'Action'
        COMEDY = 'Comedy', 'Comedy'
        DRAMA = 'Drama', 'Drama'
        OTHER = 'Other', 'Other'

    title = models.CharField(
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(50)
        ]
    )
    release_date = models.DateField()

    storyline = models.TextField(
        null=True,
    )
    genre = models.CharField(
        choices=GenreChoices.choices,
        validators=[
            MaxLengthValidator(6),
        ],
        default="Other"
    )
    rating = models.DecimalField(
        3,
        1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ],
        default=0.0
    )
    is_classic = models.BooleanField(
        default=False
    )
    is_awarded = models.BooleanField(
        default=False
    )
    last_updated = models.DateField(
        auto_now=True
    )
    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
    )
    starring_actor = models.ForeignKey(
        to=Actor,
        null=True,
        on_delete=models.SET_NULL
    )
    actors = models.ManyToManyField(
        to=Actor,
    )
