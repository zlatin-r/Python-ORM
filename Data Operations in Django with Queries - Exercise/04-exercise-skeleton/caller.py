import os
import django
from django.db.models import QuerySet, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# from populate_db import populate_model_with_data
# populate_model_with_data(HotelRoom, 10)


# Create queries within functions


def create_pet(name: str, species: str) -> str:
    pet = Pet.objects.create(
        name=name,
        species=species
    )

    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )

    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str) -> None:
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()

    # Artifact.objects.filter(is_magical=True, age__gt=250, pk=artifact.pk).update(name=new_name)


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()


def show_all_locations() -> str:
    locations = Location.objects.all().order_by('-id')

    return "\n".join(str(l) for l in locations)


def new_capital() -> None:
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()


def apply_discount() -> None:
    cars = Car.objects.all()
    for car in cars:
        discount_percentage = sum(int(x) for x in str(car.year)) / 100
        discount = float(car.price) * discount_percentage
        car.price_with_discount = float(car.price) - discount
        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.all().filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


def show_unfinished_tasks() -> str:
    tasks = Task.objects.filter(is_finished=False)

    return '\n'.join(str(t) for t in tasks)


def complete_odd_tasks() -> None:
    tasks = Task.objects.all()
    for task in tasks:
        if task.pk % 2 == 1:
            task.is_finished = True
            task.save()

    # Task.objects.bulk_update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(symbol) - 3) for symbol in text)

    # Task.objects.filter(title=task_title).update(description=decoded_text)

    tasks = Task.objects.filter(title=task_title)

    for task in tasks:
        task.description = decoded_text
        task.save()

    # Task.objects.bulk_update(tasks, ['description'])


def get_deluxe_rooms() -> str:
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    rooms = []

    for room in deluxe_rooms:
        if room.id % 2 == 0:
            rooms.append(room)

    return '\n'.join(str(room) for room in rooms)


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by('id')

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity is not None:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

    HotelRoom.objects.bulk_update(rooms, ['capacity'])


def reserve_first_room() -> None:
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room() -> None:
    room = HotelRoom.objects.last()

    if not room.is_reserved:
        room.delete()


def update_characters() -> None:
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7,
    )
    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4,
    )
    Character.objects.filter(class_name__in=['Assassin', 'Scout']).update(
        inventory='Inventory is empty',
    )

    # characters = Character.objects.all()
    #
    # for character in characters:
    #     if character.class_name == 'Mage':
    #         character.level += 3
    #         character.intelligence -= 7
    #         character.save()
    #
    #     elif character.class_name == 'Warrior':
    #         character.hit_points = character.hit_points / 2
    #         character.dexterity += 4
    #         character.save()
    #     else:
    #         character.inventory = 'The inventory is empty'
    #         character.save()


def fuse_characters(first_character: Character, second_character: Character) -> None:
    new_character = Character
    new_character.name = f"{first_character.name} {second_character.name}"
    new_character.class_name = "Fusion"
    new_character.level = (first_character.level + second_character.level) // 2
    new_character.strength = (first_character.strength + second_character.strength) * 1.2
    new_character.dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    new_character.intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    new_character.hit_points = first_character.hit_points + second_character.hit_points
    first_fusion_character = Character.objects.filter(class_name='Fusion').first()


def grand_dexterity() -> None:
    Character.objects.update(dexterity=30)


def grant_intelligence() -> None:
    Character.objects.update(intelligence=40)


def grant_strength() -> None:
    Character.objects.update(strength=50)


def delete_characters() -> None:
    Character.objects.filter(inventory='The inventory is empty').delete()
