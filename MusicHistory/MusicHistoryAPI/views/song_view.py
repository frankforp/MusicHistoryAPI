from django.shortcuts import render
from MusicHistoryAPI import serializers
from rest_framework import viewsets
from MusicHistoryAPI.models import *
from MusicHistoryAPI.serializers import *

class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Songs to be viewed or edited.
    """
    queryset = song_model.Song.objects.all().order_by('-song_title')
    serializer_class = song_serializer.SongSerializer
