import os
import django
from django.db.models import Count

from poulate import populate_model_with_data

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Tournament, Match


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
    top_player = TennisPlayer.objects.annotate(
        count_wins=Count("winner")).order_by("-count_wins", "full_name").first()

    if not top_player:
        return ""

    return f"Top Tennis Player: {top_player.full_name} with {top_player.count_wins} wins."


# print(get_top_tennis_player())
def get_tennis_player_by_matches_count():
    top_player = TennisPlayer.objects.annotate(
        count_matches=Count("matches")).order_by("-count_matches", "ranking").first()

    if not top_player or not top_player.count_matches:
        return ""

    return f"Tennis Player: {top_player.full_name} with {top_player.count_matches} matches played."


def get_tournaments_by_surface_type(surface=None):
    tournaments = Tournament.objects.all().annotate(
        count_matches=Count("matches")).filter(surface_type__icontains=surface).order_by("-start_date")

    if not tournaments or not surface:
        return ""

    result = [f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.count_matches}"
              for t in tournaments]

    return "\n".join(result)


print(get_tournaments_by_surface_type("Grass"))


def get_latest_match_info():
    latest_match = Match.objects.prefetch_related("players", "tournament").order_by("-date_played").first()

    if not latest_match:
        return ""

    players = latest_match.players.all()
    player_one = players.first().full_name
    player_two = players.last().full_name
    winner = latest_match.winner.full_name if latest_match.winner else "TBA"

    return (f"Latest match played on: {latest_match.date_played}, "
            f"tournament: {latest_match.tournament.name}, "
            f"score: {latest_match.score}, "
            f"players: {player_one} vs {player_two}, "
            f"winner: {winner}, "
            f"summary: {latest_match.summary}")


# print(get_latest_match_info())


def get_matches_by_tournament(tournament_name=None):
    pass
