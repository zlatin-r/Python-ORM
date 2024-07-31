from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from main_app.mixins import PersonInfo


# Create your models here.
class Director(PersonInfo):
    years_of_experience = models.SmallIntegerField(validators=[MinValueValidator(0)], default=0)


class Actor(PersonInfo):
    is_awarded = models.BooleanField(default=False)