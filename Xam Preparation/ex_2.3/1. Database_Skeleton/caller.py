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
            | Q(email__icontains=search_string) \
            | Q(phone_number__icontains=search_string)

    profiles = Profile.objects.filter(query).order_by('full_name')

    if not profiles.exists():
        return ""

    result = [(f"Profile: {p.full_name}, "
               f"email: {p.email}, "
               f"phone number: {p.phone_number}, "
               f"orders: {p.order_profiles.count()}")
              for p in profiles]

    return "\n".join(result)


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ""

    result = [f"Profile: {p.full_name}, orders: {p.order_profiles.count()}" for p in profiles]

    return "\n".join(result)


def get_last_sold_products():
    order = Order.objects.order_by("creation_date").last()

    if not order or order.products.count() == 0:
        return ""

    products = ", ".join(p.name for p in order.products.all())

    return f"Last sold products: {products}"
