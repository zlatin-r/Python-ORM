from django.core.validators import MinLengthValidator
from django.db import models


class NameMixin(models.Model):
    name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])

    class Meta:
        abstract = True
