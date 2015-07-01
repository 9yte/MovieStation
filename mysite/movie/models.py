from django.db import models
from django.conf import settings
# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator


class Crew(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Movie(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(blank=True, null=False)
    IMDB_link = models.CharField(max_length=100)
    cover_photo = models.ImageField(upload_to='movie_covers', null=True, blank=True)
    rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True)
    rate_numbers = models.FloatField(default=0)
    crews = models.ManyToManyField(Crew, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)