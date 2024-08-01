import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order


# Create queries within functions

def get_profiles(search_string=None):
    if search_string is None:
        return ""

    query = Q(full_name__icontains=search_string) \
            | Q(email__icontains=search_string) \
            | Q(phone_number__icontains=search_string)

    profiles = Profile.objects.filter(query).order_by('full_name')

    if not profiles:
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


def get_top_products():
    products = Product.objects.annotate(count_orders=Count("order_products")) \
                   .filter(count_orders__gt=0) \
                   .order_by('-count_orders', 'name')[:5]

    if not products:
        return ""

    return f"Top products:\n{'\n'.join([f"{p.name}, sold {p.count_orders} times" for p in products])}"


def apply_discounts():
    orders = Order.objects.annotate(count_products=Count("products")) \
        .filter(is_completed=False, count_products__gt=2) \
        .update(total_price=F("total_price") * 0.90)

    num_updated = orders.count()

    return f"Discount applied to {num_updated} orders."


def complete_order():
    order = Order.objects.order_by("creation_date").filter(is_completed=False).last().update(is_completed=True)
