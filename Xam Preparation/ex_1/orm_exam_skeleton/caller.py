import os
import django
from django.db.models import Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models here

# Create queries within functions

def get_directors(search_name=None, search_nationality=None):
    if Q(search_name is None) & Q(search_nationality is None):
        return ""
