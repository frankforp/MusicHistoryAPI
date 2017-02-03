from rest_framework import serializers
from MusicHistoryAPI.models import *


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a hyperlinked serializer for the Artist model
    """
    class Meta:
        model = artist_model.Artist
        fields = ('artist_name',)


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a hyperlinked serializer for the Album model
    """
    class Meta:
        model = album_model.Album
        fields = ('album_title', 'album_release_date', 'artist',)


class SongSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a hyperlinked serializer for the Song model
    """
    class Meta:
        model = song_model.Song
        fields = ('song_title', 'song_length', 'song_release_date', 'genre', 'album', 'artist',)


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a hyperlinked Serializer for the Genre model
    """
    class Meta:
        model = genre_model.Genre
        fields = ('genre_name',)




