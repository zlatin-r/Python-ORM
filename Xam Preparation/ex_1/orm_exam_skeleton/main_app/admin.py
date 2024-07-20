from django.contrib import admin

from main_app.models import Director, Actor, Movie


# Register your models here.

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'nationality')
    list_fiter = ('years_of_experience',)
    list_search_fields = ('full_name', 'nationality')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'nationality')
    list_fiter = ('is_awarded',)
    list_search_fields = ('full_name',)
    readonly_fields = ('last_updated',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'storyline', 'rating', 'director')
    list_fiter = ('is_awarded', 'is_classic', 'genre')
    list_search_fields = ('title', 'full_name')
    readonly_fields = ('last_updated',)
