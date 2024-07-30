from django.db import models


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self):
        pass
