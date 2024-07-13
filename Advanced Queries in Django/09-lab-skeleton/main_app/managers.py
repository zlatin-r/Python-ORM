from django.db import models

from main_app.models import Product


class ProductManager(models.Manager):

    def available_products(self):
        available = Product.objects.filter(is_available=True)
        return available

    def available_products_in_category(self, category_name: str):
        all_products_in_category = Product.objects.filter(category_name=category_name, is_available=True)
        return all_products_in_category
