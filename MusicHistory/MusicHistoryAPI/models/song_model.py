from django.db import models
from . import genre_model, album_model, artist_model

class Song(models.Model):
    """
    The Song table maintains Songs' Genres, artists, and albums
    """
    song_title = models.CharField(max_length=128)
    song_length = models.CharField(max_length=128)
    song_release_date = models.DateField()
    genre = models.ForeignKey(genre_model.Genre, on_delete=models.CASCADE)
    album = models.ForeignKey(album_model.Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(artist_model.Artist, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Songs'

    def __str__(self):
        return str(self.song_title)
