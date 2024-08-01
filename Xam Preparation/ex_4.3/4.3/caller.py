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
    if surface is None:
        return ""

    tournaments = Tournament.objects.all() \
        .annotate(count_matches=Count("matches")) \
        .filter(surface_type__icontains=surface) \
        .order_by("-start_date")

    result = [f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.count_matches}"
              for t in tournaments]

    return "\n".join(result) if result else ""


def get_latest_match_info():
    match = Match.objects.select_related("tournament", "winner") \
        .prefetch_related("players") \
        .order_by("-date_played", "id").first()

    if not match:
        return ""

    players = match.players.all()
    pl1 = players.first().full_name
    pl2 = players.last().full_name
    winner = match.winner.full_name if match.winner else "TBA"

    return (f"Latest match played on: {match.date_played}, "
            f"tournament: {match.tournament.name}, "
            f"score: {match.score}, "
            f"players: {pl1} vs {pl2}, "
            f"winner: {winner}, "
            f"summary: {match.summary}")


def get_matches_by_tournament(tournament_name=None):
    if not tournament_name:
        return "No matches found."

    matches = Match.objects.all().filter(tournament__name=tournament_name).order_by("-date_played")

    if not matches:
        return "No matches found."

    result = [(f"Match played on: {m.date_played}, "
               f"score: {m.score}, "
               f"winner: {'TBA' if not m.winner else m.winner.full_name}")
              for m in matches]

    return "\n".join(result)
