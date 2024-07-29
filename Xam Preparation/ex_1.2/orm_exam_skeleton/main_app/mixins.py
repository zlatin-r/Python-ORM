from django.core.validators import MinLengthValidator
from django.db import models


class PersonInfoMixin(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default="1900-01-01")
    nationality = models.CharField(max_length=50, default="Unknown")


class IsAwarded(models.Model):
    is_awarded = models.BooleanField(default=False)


class LastUpdated(models.Model):
    last_updated = models.DateTimeField(auto_now=True)