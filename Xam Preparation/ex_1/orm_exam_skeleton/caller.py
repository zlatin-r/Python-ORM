import os
import django
from django.db.models import Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Director


# Create queries within functions

def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    query_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)

    if search_name is not None and search_nationality is not None:
        query = Q(query_name & query_nationality)
    elif search_name is not None:
        query = Q(query_name)
    else:
        query = Q(query_nationality)
