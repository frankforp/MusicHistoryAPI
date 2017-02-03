from django.db import models

class Genre(models.Model):
    """
    The Genre table maintains the Genres of Songs
    """
    genre_name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Genres'

    def __str__(self):
        return str(self.genre_name)
