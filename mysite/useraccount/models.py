from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings


class UserProfile(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    follow = models.ManyToManyField("self", through='Follow', blank=True, symmetrical=False)
    #followers = models.ManyToManyField("self", blank=True)
    activation_code = models.CharField(max_length=100, default=1)
    nickname = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    objects = UserManager()

    def __str__(self):
        return "{}".format(self.username)


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='followings')
    followed = models.ForeignKey(UserProfile, related_name='followers')