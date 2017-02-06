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
