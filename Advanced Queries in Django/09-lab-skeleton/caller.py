import os
import django
from django.db.models import Sum

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct


# Create and run queries
# Task 1:
#
# print('All Products:')
# print(Product.objects.all())
# print()
# print('All Available Products:')
# print(Product.objects.available_products())
# print()
# print('All Available Food Products:')
# print(Product.objects.available_products_in_category("Food"))
# --------------------------------------------------------------------
# Task 2:

def product_quantity_ordered():
    result = []

    orders = Product.objects.annotate(
        total=Sum("orderproduct__quantity")
    ).values("name", "total"
             ).order_by("-total")

    for order in orders:
        result.append(f'Quantity ordered of {order["name"]}: {order["total"]}')

    return "\n".join(result)


print(product_quantity_ordered())
