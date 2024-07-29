import os
import django
from django.db.models import Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order


# Create queries within functions

def get_profiles(search_string=None):
    if not search_string:
        return ""

    query = Q(full_name__icontains=search_string) \
            | \
            Q(email__icontains=search_string) \
            | \
            Q(phone__icontains=search_string)

    profiles = Profile.objects.all().filter(query).order_by('full_name')

    if not profiles:
        return ""

    result = [f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number1}, orders: {p.count_orders}"
              for p in profiles]

    return "\n".join(result)

def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ""

    result = [f"Profile: {p.full_name}, orders: {p.count_orders}" for p in profiles]

    return "\n".join(result)


def get_last_sold_products():
    latest_order = Order.objects.prefetch_related("products").last()

    if not latest_order or not latest_order.products:
        return ""

    products = ", ".join(latest_order.products.all().order_by("name"))

    return f"Last sold products: {products}"
