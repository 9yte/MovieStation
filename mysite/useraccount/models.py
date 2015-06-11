from django.db import models


from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings


class UserProfile(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    followings = models.ManyToManyField("self")
    followers = models.ManyToManyField("self")
    activation_code = models.CharField(max_length=100, default=1)
    nickname = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to=settings.UPLOAD_URL + '/avatars', null=True, blank=True)
    objects = UserManager()

    def __str__(self):
        return "{}".format(self.username)


class Movie(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=False)
    IMDB_link = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)


class Post(models.Model):
    author = models.ForeignKey(UserProfile)
    image = models.ImageField(upload_to=settings.UPLOAD_URL + '/post_images')
    movie = models.ForeignKey(Movie)
    rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    text = models.TextField(blank=True, null=False)
    date_time = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return "{}".format(self.text)


class Comment(models.Model):
    author = models.ForeignKey(UserProfile)
    date_time = models.DateTimeField(blank=False, null=False)
    text = models.CharField(max_length=350)
    post = models.ForeignKey(Post)

    def __str__(self):
        return "{}".format(self.text)


class Favourite(models.Model):
    user = models.ForeignKey(UserProfile)
    post = models.ForeignKey(Post)

    def __str__(self):
        return "{}".format(self.user.nickname)