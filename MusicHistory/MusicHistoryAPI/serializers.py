from rest_framework import serializers
from MusicHistoryAPI import models

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    pass

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    pass

class SongSerializer(serializers.HyperlinkedModelSerializer):
    pass

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    pass




