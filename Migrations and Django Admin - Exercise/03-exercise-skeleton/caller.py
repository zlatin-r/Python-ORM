import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Shoe

print(Shoe.objects.values_list('brand', flat=True).distinct())
# Create queries within functions
