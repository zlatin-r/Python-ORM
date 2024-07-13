import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct


# Create and run queries
# Task 1:
print('All Products:')
print(Product.objects.all())
print()
print('All Available Products:')
print(Product.objects.available_products())
print()
print('All Available Food Products:')
print(Product.objects.available_products_in_category("Food"))
