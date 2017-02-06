from django.shortcuts import render
from MusicHistoryAPI import serializers
from rest_framework import viewsets
from MusicHistoryAPI.models import *
from MusicHistoryAPI.serializers import *

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Genres to be viewed or edited.
    """
    queryset = genre_model.Genre.objects.all().order_by('-genre_name')
    serializer_class = genre_serializer.GenreSerializer
