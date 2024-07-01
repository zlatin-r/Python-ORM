import os
from typing import List

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer


def show_highest_rated_art() -> str:
    highest_rated = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return f"{highest_rated.art_name} is the highest-rated art with a {highest_rated.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    artworks = [first_art, second_art]

    ArtworkGallery.objects.bulk_create(artworks)


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    most_expensive_laptop = Laptop.objects.order_by('-price', '-id').first()
    return f"{most_expensive_laptop.brand} is the most expensive laptop available for {most_expensive_laptop.price}$!"


def bulk_create_laptops(args):
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems():
    Laptop.objects.filter(brand="Asus").update(operation_system="Windows")
    Laptop.objects.filter(brand="Apple").update(operation_system="MacOS")
    Laptop.objects.filter(brand__in=["Dell", "Acer"]).update(operation_system="Linux")
    Laptop.objects.filter(brand="Lenovo").update(operation_system="Chrome OS")


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(args: List[ChessPlayer]) -> None:
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players() -> None:
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title='GM').update(games_won=30)


def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title='IM')


def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title='FM')


def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(rating__range=[0, 2199]).update(title='regular player')
