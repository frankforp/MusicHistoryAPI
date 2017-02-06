from django.shortcuts import render
from MusicHistoryAPI import serializers
from rest_framework import viewsets
from MusicHistoryAPI.models import *
from MusicHistoryAPI.serializers import *


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Albums to be viewed or edited.
    """
    queryset = album_model.Album.objects.all().order_by('-album_title')
    serializer_class = album_serializer.AlbumSerializer
