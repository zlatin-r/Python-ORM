import os
from pprint import pprint

import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Author


# Create queries within functions

def get_authors(search_name=None, search_email=None):
    authors_matched = None

    if search_name is None and search_email is None:
        return ""

    if search_name and search_email:
        authors_matched = Author.objects.all().filter(full_name__icontains=search_name, email__icontains=search_email)

    elif search_name and search_email is None:
        authors_matched = Author.objects.all().filter(full_name__icontains=search_name)

    elif search_email and search_name is None:
        authors_matched = Author.objects.all().filter(email__icontains=search_email)

    if authors_matched is None:
        return ""

    result = []

    for a in authors_matched.order_by('-full_name'):
        result.append(f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}")

    return "\n".join(result)


def get_top_publisher():
    top_author = Author.objects.get_authors_by_article_count().first()

    if top_author.article_count > 0:
        return (f"Top Author: {top_author.full_name} "
                f"with {top_author.article_count} published articles.")
    else:
        return ""


def get_top_reviewer():
    top_author = Author.objects.annotate(count_reviews=Count('reviews')).order_by('email').first()

    if top_author.count_reviews > 0:
        return (f"Top Reviewer: {top_author.full_name} "
                f"with {top_author.count_reviews} published reviews.")
    else:
        return ""

# for a in Author.objects.get_authors_by_article_count():
#     print(f"name: {a.full_name}, article count: {a.article_count}")
# print(get_top_publisher())
