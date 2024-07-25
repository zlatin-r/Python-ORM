import os
import django
from django.db.models import Count

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


def get_top_tennis_player():
    top_player = TennisPlayer.objects.annotate(count_wins=Count("winner")).order_by("-count_wins", "full_name").first()

    if not top_player:
        return ""

    return f"Top Tennis Player: {top_player.full_name} with {top_player.count_wins} wins."


# print(get_top_tennis_player())
