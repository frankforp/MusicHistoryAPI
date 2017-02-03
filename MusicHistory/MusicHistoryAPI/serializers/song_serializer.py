# from django.contrib.auth.models import Group
from rest_framework import serializers
from MusicHistoryAPI.models import *


class SongSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a hyperlinked serializer for the Song model
    """
    class Meta:
        model = song_model.Song
        fields = ('song_title', 'song_length', 'song_release_date', 'genre', 'album', 'artist',)
