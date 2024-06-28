import os
import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task
from populate_db import populate_model_with_data


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
        if task.pk % 2 == 0:
            task.is_finished = True
            task.save()

    # Task.objects.bulk_update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str) -> None:
    tasks = Task.objects.filter(Task.title == task_title)
    new_title = ''

    for i in range(len(text)):
        new_title += ord(text[i + 3])

    for task in tasks:
        task.title = new_title
        task.save()


encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
