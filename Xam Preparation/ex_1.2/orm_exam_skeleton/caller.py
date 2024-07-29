import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


# Create queries within functions

def get_directors(search_name=None, search_nationality=None):
    directors = None

    if not search_name and not search_nationality:
        return ""
    elif search_name and search_nationality:
        directors = Director.objects.filter(full_name__icontains=search_name,
                                            nationality__icontains=search_nationality)
    elif search_name and not search_nationality:
        directors = Director.objects.filter(full_name__icontains=search_name)
    elif not search_name and search_nationality:
        directors = Director.objects.filter(nationality__icontains=search_nationality)

    if not directors:
        return ""

    result = [f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}"
              for d in directors]

    return "\n".join(result)

