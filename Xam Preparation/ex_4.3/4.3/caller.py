import os
import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Tournament, Match


# Create queries within functions

def get_tennis_players(search_name=None, search_country=None):
    if not search_name and not search_country:
        return ""

    query = None

    if search_name and search_country:
        query = Q(full_name__icontains=search_name) & Q(country__icontains=search_country)
    elif search_name and not search_country:
        query = Q(full_name__icontains=search_name)
    elif not search_name and search_country:
        query = Q(country__icontains=search_country)

    players = TennisPlayer.objects.filter(query).order_by("ranking")

    if not players.exists():
        return ""

    result = [f"Tennis Player: {p.full_name}, country: {p.country}, ranking: {p.ranking}" for p in players]

    return "\n".join(result)


def get_top_tennis_player():
    player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if not player:
        return ""

    return f"Top Tennis Player: {player.full_name} with {player.count_wins} wins."


def get_tennis_player_by_matches_count():
    player = TennisPlayer.objects.annotate(count_matches=Count("matches")).order_by("-count_matches", "ranking").first()

    if not player or player.count_matches == 0:
        return ""

    return f"Tennis Player: {player.full_name} with {player.count_matches} matches played."


def get_tournaments_by_surface_type(surface=None):
    if not surface:
        return ""

    tournaments = Tournament.objects.annotate(count_matches=Count("matches")) \
                                    .filter(surface_type__icontains=surface) \
                                    .order_by("-start_date")

    if not tournaments:
        return ""

    result = [f"Tournament: {t.name}, start date: {t.start_date}, matches: {s.count_matches}"
              for t in tournaments]

    return "\n".join(result)
