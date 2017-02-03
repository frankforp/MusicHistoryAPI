from django.contrib import admin
from MusicHistoryAPI.models import artist_model, album_model, genre_model, song_model


admin.site.register(artist_model.Artist)
admin.site.register(album_model.Album)
admin.site.register(genre_model.Genre)
admin.site.register(song_model.Song)
