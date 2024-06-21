from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(
        max_length=30
    )
    age = models.PositiveIntegerField()


class WeatherForecast(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
