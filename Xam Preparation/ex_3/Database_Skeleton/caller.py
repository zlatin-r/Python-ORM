import os
from pprint import pprint

import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Author, Article


# Create queries within functions

def get_authors(search_name=None, search_email=None):
    authors_matched = None

    if search_name and search_email:
        authors_matched = Author.objects.all().filter(
            Q(full_name__icontains=search_name)
            &
            Q(email__icontains=search_email))

    elif search_name and search_email is None:
        authors_matched = Author.objects.all().filter(
            Q(full_name__icontains=search_name)
        )

    elif search_email and search_name is None:
        authors_matched = Author.objects.all().filter(
            Q(email__icontains=search_email)
        )

    if search_name is None and search_email is None:
        return ""

    if authors_matched is None:
        return ""

    result = []

    for a in authors_matched.order_by('-full_name'):
        result.append(f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}")

    return "\n".join(result)


def get_top_publisher():
    top_author = Author.objects.get_authors_by_article_count().first()

    if not top_author:
        return ""

    if top_author.article_count > 0:
        return (f"Top Author: {top_author.full_name} "
                f"with {top_author.article_count} published articles.")
    else:
        return ""


def get_top_reviewer():
    top_author = Author.objects.annotate(count_reviews=Count('reviews')).order_by('-count_reviews', 'email').first()

    if not top_author:
        return ""

    if top_author.count_reviews > 0:
        return (f"Top Reviewer: {top_author.full_name} "
                f"with {top_author.count_reviews} published reviews.")
    else:
        return ""


def get_latest_article():
    last_article = Article.objects.prefetch_related('authors', 'reviews').order_by('-published_on').first()

    if not last_article:
        return ""

    authors = ", ".join(a.full_name for a in last_article.authors.all().order_by('full_name'))
    num_reviews = last_article.reviews.count()
    avg_reviews = sum([v.rating for v in last_article.reviews.all()]) / num_reviews if num_reviews else 0.0

    return (f"The latest article is: {last_article.title}. "
            f"Authors: {authors}. "
            f"Reviewed: {num_reviews} times. "
            f"Average Rating: {avg_reviews:.2f}.")


def get_top_rated_article():
    top_rated_article = Article.objects.annotate(avg_rating=Avg('reviews__rating')) \
        .order_by('-avg_rating', 'title') \
        .first()

    num_reviews = top_rated_article.reviews.count() if top_rated_article else 0
    if top_rated_article is None or num_reviews == 0:
        return ""

    avg_rating = top_rated_article.avg_rating or 0.0

    return f"The top-rated article is: {top_rated_article.title}, " \
           f"with an average rating of {avg_rating:.2f}, " \
           f"reviewed {num_reviews} times."


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    author = Author.objects.filter(email=email).first()

    if not author:
        return "No authors banned."

    num_reviews = author.reviews.count()

    author.is_banned = True
    author.reviews.all().delete()
    author.save()

    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."


# a = Author.objects.get(full_name="Author 5")
# print(a.reviews.count())

# a = Author.objects.get(email="Author 1")
# print(a.reviews.count())
# print(ban_author("Author 1"))
# print(a.reviews.count())
# print(a.is_banned)

print(ban_author("Author 111"))
