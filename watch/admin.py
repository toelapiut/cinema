from django.contrib import admin
from .models.genre import Genre
from .models.movie import Movie


# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """ Movie admin"""
    list_display = ('title', 'summary', 'release_date', 'rating', 'runtime', 'created_at')
    search_fields = ('title', 'summary')
    filter_horizontal = ('genre',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genre admin."""
    list_display = ('name',)
    search_fields = ('name',)
