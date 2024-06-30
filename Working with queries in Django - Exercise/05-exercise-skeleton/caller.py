import os
from typing import List

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop


def show_highest_rated_art() -> str:
    highest_rated = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return f"{highest_rated.art_name} is the highest-rated art with a {highest_rated.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    artworks = [first_art, second_art]

    ArtworkGallery.objects.bulk_create(artworks)


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()


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


