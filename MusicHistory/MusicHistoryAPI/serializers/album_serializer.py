# from django.contrib.auth.models import Group
from rest_framework import serializers
from MusicHistoryAPI.models import *

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a hyperlinked serializer for the Album model
    """
    class Meta:
        model = album_model.Album
        fields = ('album_title', 'album_release_date', 'artist',)
