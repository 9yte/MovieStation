from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Post(models.Model):
    author = models.ForeignKey('useraccount.UserProfile')
    movie = models.ForeignKey('movie.Movie')
    rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    text = models.TextField()
    date_time = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return "{}".format(self.text)


class Comment(models.Model):
    author = models.ForeignKey('useraccount.UserProfile')
    date_time = models.DateTimeField(blank=False, null=False)
    text = models.CharField(max_length=350)
    post = models.ForeignKey(Post)

    def __str__(self):
        return "{}".format(self.text)


class Favourite(models.Model):
    user = models.ForeignKey('useraccount.UserProfile')
    post = models.ForeignKey(Post)
    date_time = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return "{}".format(self.user.nickname)