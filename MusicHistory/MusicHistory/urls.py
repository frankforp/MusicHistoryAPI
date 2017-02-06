from django.conf.urls import url, include
from django.contrib import admin
from MusicHistoryAPI.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'artists', artist_view.ArtistViewSet)
router.register(r'albums', album_view.AlbumViewSet)
router.register(r'songs', song_view.SongViewSet)
router.register(r'genre', genre_view.GenreViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
