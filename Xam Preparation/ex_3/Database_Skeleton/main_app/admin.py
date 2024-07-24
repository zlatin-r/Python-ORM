from django.contrib import admin

from main_app.models import Author, Article, Review


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
