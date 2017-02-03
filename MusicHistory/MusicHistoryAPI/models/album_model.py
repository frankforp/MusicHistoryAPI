from django.db import models
from . import artist_model

class Album(models.Model):
    """
    The Album table maintains Albums' Artists and Songs
    """
    album_title = models.CharField(max_length=128)
    album_release_date = models.DateField()
    artist = models.ForeignKey(artist_model.Artist, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Albums'

    def __str__(self):
        return str(self.album_title)
