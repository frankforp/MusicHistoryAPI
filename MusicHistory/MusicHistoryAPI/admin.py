from django.contrib import admin
from MusicHistoryAPI.models import Artist, Album, Genre, Song


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Song)
