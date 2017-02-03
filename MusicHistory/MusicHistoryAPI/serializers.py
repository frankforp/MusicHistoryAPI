from rest_framework import serializers
from MusicHistoryAPI import models

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a hyperlinked serializer for the Artist model
    """
    class Meta:
        model = models.Artist
        fields = ('artist_name',)


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a hyperlinked serializer for the Album model
    """
    class Meta:
        model = models.Album
        fields = ('album_title', 'album_release_date', 'artist',)


class SongSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a hyperlinked serializer for the Song model
    """
    class Meta:
        model = models.Song
        fields = ('song_title', 'song_length', 'song_release_date', 'genre', 'album', 'artist',)


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    Creates a hyperlinked Serializer for the Genre model
    """
    class Meta:
        model = models.Genre
        fields = ('genre_name',)




