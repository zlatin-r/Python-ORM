import os
from pprint import pprint

import django
from django.db.models import Q, Count

from main_app.managers import AuthorManager

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Author


# Create queries within functions

def get_authors(search_name=None, search_email=None):
    authors_matched = None

    if search_name and search_email:
        authors_matched = Author.objects.all().filter(
            Q(full_name__icontains=search_name)
            |
            Q(email__icontains=search_email))

    if search_name and not search_email:
        authors_matched = Author.objects.all().filter(
            Q(full_name__icontains=search_name)
        )

    if search_email and not search_name:
        authors_matched = Author.objects.all().filter(
            Q(email__icontains=search_email)
        )

    if (not search_email and not search_name) or not authors_matched:
        return ""

    result = []

    for a in authors_matched.order_by('-full_name'):
        result.append(f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}")

    return "\n".join(result)


def get_top_publisher():
    top_author = Author.objects.get_authors_by_article_count().first()

    return (f"Top Author: {top_author.full_name} "
            f"with {top_author.article_count} published articles.") if top_author else ""


def get_top_reviewer():
    top_author = Author.objects.annotate(count_reviews=Count('reviews')).order_by('email').first()

    return (f"Top Reviewer: {top_author.full_name} "
            f"with {top_author.count_reviews} published reviews.") if top_author else ""


# for a in Author.objects.get_authors_by_article_count():
#     print(f"name: {a.full_name}, article count: {a.article_count}")
# print(get_top_publisher())
