from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from main_app.mixins import CreationDateMixin, TotalPriceMixin


# Create your models here.

class Profile(CreationDateMixin):
    full_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=True)


class Product(TotalPriceMixin):
    name = models.CharField(max_length=100)
    description = models.TextField()
    in_stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)


class Order(TotalPriceMixin, CreationDateMixin):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    is_completed = models.BooleanField(default=False)
