import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from poulate import populate_model_with_data
from main_app.models import Director, Actor, Movie

# Create queries within functions

populate_model_with_data(Director)