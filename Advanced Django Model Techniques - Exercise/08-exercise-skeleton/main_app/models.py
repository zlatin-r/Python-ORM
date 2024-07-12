from django.db import models
from .validators import ValidateName


# Create your models here.

class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            ValidateName("Name can only contain letters and spaces")
        ]
    )
