# from django.contrib.auth.models import Group
from rest_framework import serializers
from MusicHistoryAPI.models import *


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a hyperlinked serializer for the Artist model
    """
    class Meta:
        model = artist_model.Artist
        fields = ('artist_name',)
