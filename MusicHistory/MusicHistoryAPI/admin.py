from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from MusicHistoryAPI.models import Artist, Album, Genre, Song

# Register your models here.
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Song)
