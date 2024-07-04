import os
from datetime import timedelta, date

import django.utils.timezone as timezone
import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Registration, Car


# Create queries within functions

def show_all_authors_with_their_books() -> str:
    result = []
    authors = Author.objects.all().order_by("id")

    for author in authors:
        books = author.book_set.all()  # Book.object.filter(author=author)

        if books:
            book_title = ", ".join([book.title for book in books])
            result.append(f"{author.name} has written - {book_title}!")

    return "\n".join(result)


def delete_all_authors_without_books() -> None:
    authors_without_books = Author.objects.filter(book__isnull=True)
    authors_without_books.delete()

    # Author.objects.filter(book__isnull=True).delete()


# # Create authors
# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")
#
# # Create books associated with the authors
# book1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     price=19.99,
#     author=author1)
# book2 = Book.objects.create(
#     title="1984",
#     price=14.99,
#     author=author2)
# book3 = Book.objects.create(
#     title="To Kill a Mockingbird",
#     price=12.99,
#     author=author3)
#
# # Display authors and their books
# authors_with_books = show_all_authors_with_their_books()
# print(authors_with_books)
#
# # Delete authors without books
# delete_all_authors_without_books()
# print(Author.objects.count())


def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)  # add(), remove(), clear()


def get_songs_by_artist(artist_name: str) -> QuerySet:
    artist = Artist.objects.get(name=artist_name)

    return artist.songs.all().order_by('-id')

    # Artist.objects.get(name=artist_name).songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


# # Create artists
# artist1 = Artist.objects.create(name="Daniel Di Angelo")
# artist2 = Artist.objects.create(name="Indila")
#
# # Create songs
# song1 = Song.objects.create(title="Lose Face")
# song2 = Song.objects.create(title="Tourner Dans Le Vide")
# song3 = Song.objects.create(title="Loyalty")
#
# # Add a song to an artist
# add_song_to_artist("Daniel Di Angelo", "Lose Face")
# add_song_to_artist("Daniel Di Angelo", "Loyalty")
# add_song_to_artist("Indila", "Tourner Dans Le Vide")
#
# # Get all songs by a specific artist
# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Daniel Di Angelo: {song.title}")
#
# # Get all songs by a specific artist
# songs = get_songs_by_artist("Indila")
# for song in songs:
#     print(f"Indila: {song.title}")
#
# # Remove a song from an artist
# remove_song_from_artist("Daniel Di Angelo", "Lose Face")
#
# # Check if the song is removed
# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Songs by Daniel Di Angelo after removal: {song.title}")


def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    total_rating = sum(review.rating for review in reviews)
    avg_rating = total_rating / len(reviews)

    return avg_rating


def get_reviews_with_high_ratings(threshold: int) -> QuerySet:
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> QuerySet:
    return Product.objects.filter(reviews=None).order_by('-name')


def delete_products_without_reviews() -> None:
    products_without_reviews = Product.objects.filter(reviews=None)
    products_without_reviews.delete()


# # Create some products
# product1 = Product.objects.create(name="Laptop")
# product2 = Product.objects.create(name="Smartphone")
# product3 = Product.objects.create(name="Headphones")
# product4 = Product.objects.create(name="PlayStation 5")
#
# # Create some reviews for products
# review1 = Review.objects.create(
#     description="Great laptop!",
#     rating=5,
#     product=product1)
# review2 = Review.objects.create(
#     description="The laptop is slow!",
#     rating=2,
#     product=product1)
# review3 = Review.objects.create(
#     description="Awesome smartphone!",
#     rating=5,
#     product=product2)
#
# # Run the function to get products without reviews
# products_without_reviews = get_products_with_no_reviews()
# print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")
#
# # Run the function to delete products without reviews
# delete_products_without_reviews()
# print(f"Products left: {Product.objects.count()}")
#
# # Calculate and print the average rating
# print(calculate_average_rating_for_product_by_name("Laptop"))

# --------------------------------------
def calculate_licenses_expiration_dates() -> str:
    result = []
    licenses = DrivingLicense.objects.all().order_by('-license_number')

    for l in licenses:
        expiration_date = l.issue_date + timedelta(days=365)
        result.append(f"License with number: {l.license_number} "
                      f"expires on {expiration_date}!")

    return "\n".join(result)


def get_drivers_with_expired_licenses(due_date: date):
    result = []

    for driver in Driver.objects.all():
        expiration_date = driver.license.issue_date + timedelta(days=365)
        if expiration_date > due_date:
            result.append(driver)

    return result


# driver1 = Driver.objects.create(first_name="Tanya", last_name="Petrova")
# driver2 = Driver.objects.create(first_name="Ivan", last_name="Yordanov")
#
# license1 = DrivingLicense.objects.create(
#     license_number="123",
#     issue_date=date(2022, 10, 6),
#     driver=driver1)
#
# license2 = DrivingLicense.objects.create(
#     license_number="456",
#     issue_date=date(2022, 1, 1),
#     driver=driver2)
#
# # Calculate licenses expiration dates
# expiration_dates = calculate_licenses_expiration_dates()
# print(expiration_dates)
#
# # Get drivers with expired licenses
# drivers_with_expired_licenses = get_drivers_with_expired_licenses(date(2023, 1, 1))
# for driver in drivers_with_expired_licenses:
#     print(f"{driver.first_name} {driver.last_name} has to renew their driving license!")

def register_car_by_owner(owner: Owner) -> str:
    registration = Registration.objects.filter(car=None).first()
    car = Car.objects.filter(registration=None).first()

    registration.registration_date = timezone.now().date()

    car.registration = registration

    registration.save()
    car.save()

    return (f"Successfully registered {car.model} "
            f"to {owner.name} "
            f"with registration number {registration.registration_number}.")

# # Create owners
# owner1 = Owner.objects.create(name='Ivelin Milchev')
# owner2 = Owner.objects.create(name='Alice Smith')
#
# # Create cars
# car1 = Car.objects.create(model='Citroen C5', year=2004)
# car2 = Car.objects.create(model='Honda Civic', year=2021)
#
# # Create instances of the Registration model for the cars
# registration1 = Registration.objects.create(registration_number='TX0044XA')
# registration2 = Registration.objects.create(registration_number='XYZ789')
# print(register_car_by_owner(owner1))
