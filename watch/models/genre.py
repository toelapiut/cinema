from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
