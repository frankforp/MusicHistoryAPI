from django.shortcuts import render
from MusicHistoryAPI import serializers
from rest_framework import viewsets
from MusicHistoryAPI.models import *
from MusicHistoryAPI.serializers import *



class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Artists to be viewed or edited.
    """
    queryset = artist_model.Artist.objects.all().order_by('-artist_name')
    serializer_class = artist_serializer.ArtistSerializer



class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Albums to be viewed or edited.
    """
    queryset = album_model.Album.objects.all().order_by('-album_title')
    serializer_class = album_serializer.AlbumSerializer



class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Songs to be viewed or edited.
    """
    queryset = song_model.Song.objects.all().order_by('-song_title')
    serializer_class = song_serializer.SongSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Genres to be viewed or edited.
    """
    queryset = genre_model.Genre.objects.all().order_by('-genre_name')
    serializer_class = genre_serializer.GenreSerializer



