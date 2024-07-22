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
    result = []
    if search_string is not None:
        profiles = Profile.objects \
            .annotate(num_orders=Count('order_profiles')) \
            .filter(Q(full_name__icontains=search_string)
                    | Q(email__icontains=search_string)
                    | Q(phone_number__icontains=search_string)) \
            .order_by('full_name')

        [result.append(f'Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, '
                       f'orders: {p.num_orders}') for p in profiles]

    return '\n'.join(result) if result else ''


def get_loyal_profiles():
    result = []

    # loyal_profiles = Profile.objects.get_regular_customers()

    profiles = Profile.objects.annotate(count_orders=Count('order_profiles')).filter(count_orders__gt=2).order_by(
        "-count_orders")

    for p in profiles:
        result.append(f"Profile: {p.full_name}, orders: {p.count_orders}")

    return "\n".join(result) if result else ""


def get_last_sold_products():
    try:
        last_order = Order.objects.prefetch_related('products').latest('creation_date')
        last_sold_products = last_order.products.all().order_by('name')

        if last_sold_products:
            last_sold_products_str = ", ".join(product.name for product in last_sold_products)
            return f"Last sold products: {last_sold_products_str}"
        return ""
    except Order.DoesNotExist:
        return ""


def get_top_products():
    top_products = Product.objects.annotate(orders_count=Count('order_profiles')
                                            ).order_by('-orders_count', "name")[:5]

    result = ["Top products:"]

    [result.append(f"{p.name}, sold {p.orders_count} times") for p in top_products]

    return "\n".join(result) if top_products else ""


def apply_discounts():
    products_to_update = Order.objects.annotate(ordered_product=Count('products')
                                                ).filter(is_completed=False).update(
        total_price=F('total_price') * 0.9)

    num_of_updated_orders = products_to_update.count()

    return f"Discount applied to {num_of_updated_orders} orders."


def complete_order():
    oldest_order = Order.objects.filter(is_completed=True).order_by('creation_date').first()

    if not oldest_order:
        return ""

    oldest_order.is_completed = True
    oldest_order.save()

    for product in oldest_order.products.all():
        product.in_stock = F('in_stock') - 1
        if product.in_stock <= 0:
            product.in_stock = 0
            product.is_available = False
        product.save()

    return "Order has been completed!"
