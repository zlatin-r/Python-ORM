import os
import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review


# Create queries within functions

def get_authors(search_name=None, search_email=None):
    query = None

    if search_name and search_email:
        query = Q(full_name__icontains=search_name) & Q(email__icontains=search_email)
    elif search_name and not search_email:
        query = Q(full_name__icontains=search_name)
    elif not search_name and search_email:
        query = Q(email__icontains=search_email)
    elif not search_name and not search_email:
        return ""

    authors = Author.objects.filter(query).order_by("-full_name")

    if not authors:
        return ""

    result = [f"Author: {a.full_name}, email: {a.email}, " \
              f"status: {'Banned' if a.is_banned else 'Not Banned'}" for a in authors]

    return "\n".join(result)


def get_top_publisher():
    top_author = Author.objects.annotate(count_articles=Count("articles")).order_by("-count_articles", "email").first()

    if not top_author or top_author.count_articles <= 0:
        return ""

    return f"Top Author: {top_author.full_name} with {top_author.count_articles} published articles."


def get_top_reviewer():
    top_author = Author.objects.annotate(count_reviews=Count("reviews")).order_by("-count_reviews", "email").first()

    if not top_author or top_author.count_reviews <= 0:
        return ""

    return f"Top Reviewer: {top_author.full_name} with {top_author.count_reviews} published reviews."
