from django.db import models


class Artist(models.Model):
    """
    The Artist table maintains the Artists' Albums and Songs
    """
    artist_name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return str(self.artist_name)
