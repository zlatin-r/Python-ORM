import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review


# Create queries within functions

def get_authors(search_name=None, search_email=None):
    if not search_name and not search_email:
        return ""

    query = None

    if search_name and search_email:
        query = Q(full_name__icontains=search_name) & Q(email__icontains=search_email)
    elif search_name and not search_email:
        query = Q(full_name__icontains=search_name)
    elif not search_name and search_email:
        query = Q(email__icontains=search_email)

    authors = Author.objects.filter(query).order_by("-full_name")

    if not authors.exists():
        return ""

    result = [f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}"
              for a in authors]

    return "\n".join(result)


def get_top_publisher():
    author = Author.objects.annotate(count_articles=Count("articles")) \
        .order_by("-count_articles", "email") \
        .first()

    if not author or author.count_articles == 0:
        return ""

    return f"Top Author: {author.full_name} with {author.count_articles} published articles."


def get_top_reviewer():
    author = Author.objects.annotate(count_reviews=Count("reviews")) \
        .order_by("-count_reviews", "email") \
        .first()

    if not author or author.count_reviews <= 0:
        return ""

    return f"Top Reviewer: {author.full_name} with {author.count_reviews} published reviews."


def get_latest_article():
    article = Article.objects \
        .prefetch_related("authors", "reviews") \
        .order_by("-published_on").first()

    if not article:
        return ""

    authors = ", ".join(a.full_name for a in article.authors.all().order_by("full_name"))
    num_reviews = article.reviews.count()
    avg_reviews = sum([r.rating for r in article.reviews.all()]) / num_reviews if num_reviews else 0.0

    return (f"The latest article is: {article.title}. "
            f"Authors: {authors}. "
            f"Reviewed: {num_reviews} times. "
            f"Average Rating: {avg_reviews:.2f}.")


def get_top_rated_article():
    article = Article.objects.annotate(avg_rating=Avg("reviews__rating")) \
        .order_by("-avg_rating", "title") \
        .first()

    num_reviews = article.reviews.count() if article else 0

    if not article or num_reviews == 0:
        return ""

    avg_rating = article.avg_rating or 0.0

    return (f"The top-rated article is: {article.title}, "
            f"with an average rating of {avg_rating:.2f}, "
            f"reviewed {num_reviews} times.")


def ban_author(email=None):
    if not email:
        return "No authors banned."

    author = Author.objects.filter(email=email).first()

    if not author:
        return "No authors banned."

    author.is_banned = True
    author.save()

    count_reviews = author.reviews.count()
    author.reviews.all().delete()

    return f"Author: {author.full_name} is banned! {count_reviews} reviews deleted."