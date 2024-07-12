from django.db import models
from .validators import validate_name


# Create your models here.

class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            validate_name
        ]
    )
