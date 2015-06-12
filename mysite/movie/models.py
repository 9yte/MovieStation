from django.db import models
from django.conf import settings
# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=False)
    IMDB_link = models.CharField(max_length=100)
    cover_photo = models.ImageField(upload_to=settings.MEDIA_ROOT + '/movie_covers', null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)