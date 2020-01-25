from django.db import models
from .movie import Movie
from .genre import Genre


class GenreTitle(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.movie.title
