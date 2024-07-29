from django.contrib import admin

from main_app.models import Actor, Director, Movie


# Register your models here.

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'nationality')
    list_filter = ('years_of_experience',)
    search_fields = ('full_name', 'nationality')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
