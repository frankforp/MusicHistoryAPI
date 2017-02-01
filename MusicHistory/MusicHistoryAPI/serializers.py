from rest_framework import serializers
from MusicHistoryAPI import models

class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Artist
        fields = '__all__'

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Album
        fields = '__all__'

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Song
        fields = '__all__'

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'




