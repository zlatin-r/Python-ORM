import os
from typing import List

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon


def show_highest_rated_art() -> str:
    highest_rated = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return f"{highest_rated.art_name} is the highest-rated art with a {highest_rated.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    artworks = [first_art, second_art]

    ArtworkGallery.objects.bulk_create(artworks)


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()


# artwork1 = ArtworkGallery(artist_name='Vincent van Gogh',
#                           art_name='Starry Night',
#                           rating=4,
#                           price=1200000.0)
# artwork2 = ArtworkGallery(artist_name='Leonardo da Vinci',
#                           art_name='Mona Lisa',
#                           rating=5,
#                           price=1500000.0)
#
# # Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)
# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())


def show_the_most_expensive_laptop() -> str:
    most_expensive = Laptop.objects.order_by('-price', '-id').first()

    return f"{most_expensive.brand} is the most expensive laptop available for {most_expensive.price}$!"


def bulk_create_laptops(args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage() -> None:
    Laptop.objects.filter(brand__in=['Asus', 'Lenovo']).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=['Apple', 'Dell']).update(memory=16)


def update_operation_systems() -> None:
    all_laptops = Laptop.objects.all()

    for laptop in all_laptops:
        if laptop.brand == "Asus":
            laptop.operation_system = "Windows"
        elif laptop.brand == "Apple":
            laptop.operation_system = "MacOS"
        elif laptop.brand in ["Dell", "Acer"]:
            laptop.operation_system = "Linux"
        elif laptop.brand == "Lenovo":
            laptop.operation_system = "Chrome OS"

        laptop.save()

    # Laptop.objects.filter(brand='Asus').update(operating_system='Windows')
    # Laptop.objects.filter(brand='Apple').update(operating_system='MacOS')
    # Laptop.objects.filter(brand__in=['Dell', 'Acer']).update(operating_system='Linux')
    # Laptop.objects.filter(brand='Lenovo').update(operating_system='Chrome OS')


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


# laptop1 = Laptop(
#     brand='Asus',
#     processor='Intel Core i5',
#     memory=8,
#     storage=256,
#     operation_system='MacOS',
#     price=899.99
# )
# laptop2 = Laptop(
#     brand='Apple',
#     processor='Chrome OS',
#     memory=16,
#     storage=256,
#     operation_system='MacOS',
#     price=1399.99
# )
# laptop3 = Laptop(
#     brand='Lenovo',
#     processor='AMD Ryzen 7',
#     memory=12,
#     storage=256,
#     operation_system='Linux',
#     price=999.99,
# )
#
# # Create a list of instances
# laptops_to_create = [laptop1, laptop2, laptop3]
#
# # Use bulk_create to save the instances
# bulk_create_laptops(laptops_to_create)
#
# update_to_512_GB_storage()
# update_operation_systems()
#
# # Retrieve 2 laptops from the database
# asus_laptop = Laptop.objects.filter(brand__exact='Asus').get()
# lenovo_laptop = Laptop.objects.filter(brand__exact='Lenovo').get()
#
# print(asus_laptop.storage)
# print(lenovo_laptop.operation_system)


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


# player1 = ChessPlayer(username='Player1',
#                       title='no title',
#                       rating=2200,
#                       games_played=50,
#                       games_won=20,
#                       games_lost=25,
#                       games_drawn=5, )
# player2 = ChessPlayer(username='Player2',
#                       title='IM',
#                       rating=2350,
#                       games_played=80,
#                       games_won=40,
#                       games_lost=25,
#                       games_drawn=15, )
#
# # Call the bulk_create_chess_players function
# bulk_create_chess_players([player1, player2])
# # Call the delete_chess_players function
# delete_chess_players()
# # Check that the players are deleted
# print("Number of Chess Players after deletion:", ChessPlayer.objects.count())


def set_new_chefs() -> None:
    Meal.objects.filter(meal_type='Breakfast').update(chef='Gordon Ramsey')
    Meal.objects.filter(meal_type='Lunch').update(chef='Julia Child')
    Meal.objects.filter(meal_type='Dinner').update(chef='Jamie Oliver')
    Meal.objects.filter(meal_type='Snack').update(chef='Thomas Keller')


def set_new_preparation_times() -> None:
    Meal.objects.filter(meal_type='Breakfast').update(preparation_time='10 minutes')
    Meal.objects.filter(meal_type='Lunch').update(preparation_time='12 minutes')
    Meal.objects.filter(meal_type='Dinner').update(preparation_time='15 minutes')
    Meal.objects.filter(meal_type='Snack').update(preparation_time='5 minutes')


def update_low_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=['Breakfast', 'Dinner']).update(calories=400)


def update_high_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).update(calories=700)


def delete_lunch_and_snack_meals() -> None:
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).delete()


# meal1 = Meal.objects.create(name="Pancakes",
#                             meal_type="Breakfast",
#                             preparation_time="20 minutes",
#                             difficulty=3,
#                             calories=350,
#                             chef="Jane", )
#
# meal2 = Meal.objects.create(name="Spaghetti Bolognese",
#                             meal_type="Dinner",
#                             preparation_time="45 minutes",
#                             difficulty=4,
#                             calories=550,
#                             chef="Sarah", )
#
# # Test the set_new_chefs function
# set_new_chefs()
#
# # Test the set_new_preparation_times function
# set_new_preparation_times()
#
# # Refreshes the instances
# meal1.refresh_from_db()
# meal2.refresh_from_db()
#
# # Print the updated meal information
# print("Meal 1 Chef:", meal1.chef)
# print("Meal 1 Preparation Time:", meal1.preparation_time)
# print("Meal 2 Chef:", meal2.chef)
# print("Meal 2 Preparation Time:", meal2.preparation_time)


def show_hard_dungeons() -> str:
    hard_dungeons = Dungeon.objects.filter(difficulty='Hard').order_by('-location')

    result = [f"{d.name} is guarded by {d.boss_name} who has {d.boss_health} health points!"
              for d in hard_dungeons]

    return '\n'.join(result)


def bulk_create_dungeons(args: List[Dungeon]) -> None:
    Dungeon.objects.bulk_create(args)


def update_dungeon_names() -> None:
    Dungeon.objects.filter(difficulty='Easy').update(name='The Erased Thombs')
    Dungeon.objects.filter(difficulty='Medium').update(name='The Coral Labyrinth')
    Dungeon.objects.filter(difficulty='Hard').update(name='The Lost Haunt')


def update_dungeon_bosses_health() -> None:

