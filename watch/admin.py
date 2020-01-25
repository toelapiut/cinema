from django.contrib import admin
from .models.genre import Genre
from .models.genreTitle import GenreTitle
from .models.movie import Movie

# Register your models here.
admin.site.register(Genre)
admin.site.register(GenreTitle)
admin.site.register(Movie)
