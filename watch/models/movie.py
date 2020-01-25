from django.db import models


class Movie(models.Model):
    """
    Handling the movie database

    TODO
    - add poster path field when creating media django app
    - create a rating system then connect it with movies models
    """

    imdb_id = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    summary = models.TextField(blank=True, max_length=500, null=True)
    release_date = models.DateTimeField(blank=True)
    rating = models.CharField(max_length=45, blank=True, null=True)
    runtime = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.title