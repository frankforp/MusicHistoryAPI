from django.db import models

class Artist(models.Model):
    """
    The Artist table maintains the Artists' Albums and Songs
    """
    # ArtistName = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Artists'

class Album(models.Model):
    """
    The Album table maintains Albums' Artists and Songs
    """
    class Meta:
        verbose_name_plural = 'Albums'

class Genre(models.Model):
    """
    The Genre table maintains the Genres of Songs
    """
    class Meta:
        verbose_name_plural = 'Genres'


class Song(models.Model):
    """
    The Song table maintains Songs' Genres, artists, and albums
    """
    class Meta:
        verbose_name_plural = 'Songs'
