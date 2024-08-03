from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator
from django.db import models

from main_app.managers import AstronautManager
from main_app.mixins import NameMixin


# Create your models here.

class Astronaut(NameMixin):
    phone_number = models.CharField(max_length=15, unique=True, validators=[RegexValidator(regex=r'^\d+$')])
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True, blank=True)
    spacewalks = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    updated_at = models.DateTimeField(auto_now=True)

    objects = AstronautManager()


class Spacecraft(NameMixin):
    manufacturer = models.CharField(max_length=100)
    capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    weight = models.FloatField(validators=[MinValueValidator(0)])
    launch_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)


class Mission(NameMixin):
    class StatusChoices(models.TextChoices):
        PLANNED = 'Planned', 'Planned'
        ONGOING = 'Ongoing', 'Ongoing'
        COMPLETED = 'Completed', 'Completed'

    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=9, choices=StatusChoices, default=StatusChoices.PLANNED)
    launch_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    spacecraft = models.ForeignKey(Spacecraft, on_delete=models.CASCADE, related_name='missions')
    astronauts = models.ManyToManyField(Astronaut, related_name='missions')
    commander = models.ForeignKey(Astronaut, on_delete=models.SET_NULL, null=True)
