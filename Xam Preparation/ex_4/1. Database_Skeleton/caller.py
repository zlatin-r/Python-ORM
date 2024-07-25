import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer


# Create queries within functions

def get_tennis_players(search_name=None, search_country=None):
    players = None

    if not search_name and not search_country:
        return ""
    elif search_name and search_country:
        players = TennisPlayer.objects.filter(full_name__icontains=search_name, country__icontains=search_country)
    elif search_name and not search_country:
        players = TennisPlayer.objects.filter(full_name__icontains=search_name)
    elif not search_name and search_country:
        players = TennisPlayer.objects.filter(country__icontains=search_country)

    if not players:
        return ""

    result = [f"Tennis Player: {p.full_name}, country: {p.country}, ranking: {p.ranking}"
              for p in players.order_by("ranking")]

    return "\n".join(result)


# print(get_tennis_players("Player 1", "Player 1"))
