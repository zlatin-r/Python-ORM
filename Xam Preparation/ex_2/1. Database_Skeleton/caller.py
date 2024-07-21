import os
import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile


# Create queries within functions

def get_profiles(search_string=None):
    result = []
    query = Q(full_name__icontains=search_string) | Q(email__icontains=search_string) | Q(
        phone_number__icontains=search_string)

    if search_string is not None:
        matched_profiles = Profile.objects.annotate(orders_count=Count('orders')).filter(query)

        [result.append(f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, "
                       f"orders: {p.orders_count}") for p in matched_profiles]

    return "\n".join(result) if result else ""


def get_loyal_profiles():
    pass
