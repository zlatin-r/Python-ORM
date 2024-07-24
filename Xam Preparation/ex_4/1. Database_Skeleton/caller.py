import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer

# Create queries within functions
# players = TennisPlayer.object.get_tennis_players_by_wins_count()
# for p in players:
#     print(p.full_name, p.wins_count)