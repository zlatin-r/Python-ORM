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
        total=Sum("orderproduct__quantity")).values("name", "total").exclude(
        total=None).order_by("-total")

    for order in orders:
        result.append(f'Quantity ordered of {order["name"]}: {order["total"]}')

    return "\n".join(result)


# print(product_quantity_ordered())
# -------------------------------------------------------------------
# Task 3:

def ordered_products_per_customer():
    prefetched_orders = Order.objects.prefetch_related('orderproduct_set__product__category').order_by('id')
    result = []

    for order in prefetched_orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")
        for order_product in order.orderproduct_set.all():
            result.append(f"- Product: {order_product.product.name},"
                          f" Category: {order_product.product.category.name}")

    return "\n".join(result)


# print(ordered_products_per_customer())
# ------------------------------------------------
# Task 4:

