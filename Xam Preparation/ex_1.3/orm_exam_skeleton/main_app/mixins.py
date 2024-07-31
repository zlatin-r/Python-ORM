from django.core.validators import MinLengthValidator
from django.db import models


class PersonInfo(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default="1900-01-01")
    nationality = models.CharField(max_length=50, default="Unknown")
