from django.shortcuts import render
from MusicHistoryAPI import serializers, models
from rest_framework import viewsets

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Artists to be viewed.
    """
    queryset = models.Artist.objects.all()


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Albums to be viewed.
    """
    queryset = models.Album.objects.all()


class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Songs to be viewed.
    """
    queryset = models.Song.objects.all()

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Genres to be viewed.
    """
    queryset = models.Genre.objects.all()


