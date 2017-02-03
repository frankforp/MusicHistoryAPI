# from django.contrib.auth.models import Group
from rest_framework import serializers
from MusicHistoryAPI.models import *

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a hyperlinked Serializer for the Genre model
    """
    class Meta:
        model = genre_model.Genre
        fields = ('genre_name',)
