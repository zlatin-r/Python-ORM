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

    if not players:
        return ""

    return "\n".join(f"Tennis Player: {p.full_name}, country: {p.country}, ranking: {p.ranking}" for p in players)


def get_top_tennis_player():
    top_p = TennisPlayer.objects.annotate(count_wins=Count("winner")).order_by("-count_wins", "full_name").first()

    if not top_p:
        return ""

    return f"Top Tennis Player: {top_p.full_name} with {top_p.count_wins} wins."


def get_tennis_player_by_matches_count():
    top_p = TennisPlayer.objects.annotate(count_matches=Count("matches")).order_by("-count_matches", "ranking").first()

    if not top_p or top_p.count_matches == 0:
        return ""

    return f"Tennis Player: {top_p.full_name} with {top_p.count_matches} matches played."


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ""

    results = Tournament.objects.all() \
        .annotate(count_matches=Count("matches")) \
        .filter(surface_type__icontains=surface) \
        .order_by("-start_date")

    result = [f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.count_matches}"
              for t in results]

    return "\n".join(result) if result else ""


def get_latest_match_info():
    latest_match = Match.objects.prefetch_related("players").order_by("-date_played", "-id").first()

    if not latest_match:
        return ""

    players = latest_match.players
    player1 = players.first().full_name
    player2 = players.last().full_name
    winner_name = "TBA" if latest_match.winner is None else latest_match.winner.full_name

    return (f"Latest match played on: {latest_match.date_played}, "
            f"tournament: {latest_match.tournament.name}, "
            f"score: {latest_match.score}, "
            f"players: {player1} vs {player2}, "
            f"winner: {winner_name}, "
            f"summary: {latest_match.summary}")


def get_matches_by_tournament(tournament_name=None):
    if not tournament_name:
        return "No matches found."

    matches = Match.objects.select_related("tournament", "winner") \
        .filter(tournament__name__exact=tournament_name) \
        .order_by("-date_played")

    if not matches:
        return "No matches found."

    result = [f"Match played on: {m.date_played}, "
              f"score: {m.score}, "
              f"winner: {m.winner.full_name if m.winner else 'TBA'}"
              for m in matches]

    return "\n".join(result)
