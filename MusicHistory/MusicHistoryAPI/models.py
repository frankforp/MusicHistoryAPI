from django.db import models

class Artist(models.Model):
    """
    The Artist table maintains the Artists' Albums and Songs
    """
    artist_name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return str(self.artist_name)

class Album(models.Model):
    """
    The Album table maintains Albums' Artists and Songs
    """
    album_title = models.CharField(max_length=128)
    album_release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Albums'

    def __str__(self):
        return str(self.album_title)

class Genre(models.Model):
    """
    The Genre table maintains the Genres of Songs
    """
    genre_name = models.CharField(max_length=128)


    class Meta:
        verbose_name_plural = 'Genres'

    def __str__(self):
        return str(self.genre_name)


class Song(models.Model):
    """
    The Song table maintains Songs' Genres, artists, and albums
    """
    song_title = models.CharField(max_length=128)
    song_length = models.CharField(max_length=128)
    song_release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)



    class Meta:
        verbose_name_plural = 'Songs'

    def __str__(self):
        return str(self.song_title)
