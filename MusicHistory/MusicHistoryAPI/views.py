from django.shortcuts import render
from MusicHistoryAPI import serializers, models
from rest_framework import viewsets

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Artists to be viewed or edited.
    """
    queryset = models.Artist.objects.all().order_by('-artist_name')
    serializer_class = serializers.ArtistSerializer



class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Albums to be viewed or edited.
    """
    queryset = models.Album.objects.all().order_by('-album_title')
    serializer_class = serializers.AlbumSerializer



class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Songs to be viewed or edited.
    """
    queryset = models.Song.objects.all().order_by('-song_title')
    serializer_class = serializers.SongSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Genres to be viewed or edited.
    """
    queryset = models.Genre.objects.all().order_by('-genre_name')
    serializer_class = serializers.GenreSerializer



