from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    email = models.EmailField()
