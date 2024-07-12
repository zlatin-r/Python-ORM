from django.db import models
from .validators import letters_and_space_validator


# Create your models here.

class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            letters_and_space_validator
        ]
    )
