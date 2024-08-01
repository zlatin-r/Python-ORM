import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models here

# Create queries within functions

def get_authors(search_name=None, search_email=None):
    pass


def get_top_publisher():
    pass


def get_top_reviewer():
    pass


