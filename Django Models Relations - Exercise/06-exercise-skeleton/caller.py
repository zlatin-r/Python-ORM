import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book


# Create queries within functions

def show_all_authors_with_their_books() -> str:
    result = []
    authors = Author.objects.all().order_by(id)

    for author in authors:
        books = author.book_set.all()

        if books:
            book_title = ", ".join([book.title for book in books])
            result.append(f"{author.name} has written - {book_title}!")

    return "\n".join(result)


def delete_all_authors_without_books() -> None:
    authors_without_books = Author.objects.filter(book__isnull=True)
    authors_without_books.delete()
