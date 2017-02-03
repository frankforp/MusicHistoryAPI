from django.shortcuts import render
from MusicHistoryAPI import serializers
from rest_framework import viewsets
from MusicHistoryAPI.models import *


class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Artists to be viewed or edited.
    """
    queryset = artist_model.Artist.objects.all().order_by('-artist_name')
    serializer_class = serializers.ArtistSerializer



class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Albums to be viewed or edited.
    """
    queryset = album_model.Album.objects.all().order_by('-album_title')
    serializer_class = serializers.AlbumSerializer



class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Songs to be viewed or edited.
    """
    queryset = song_model.Song.objects.all().order_by('-song_title')
    serializer_class = serializers.SongSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Genres to be viewed or edited.
    """
    queryset = genre_model.Genre.objects.all().order_by('-genre_name')
    serializer_class = serializers.GenreSerializer



