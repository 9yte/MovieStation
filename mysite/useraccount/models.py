from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings


class UserProfile(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    followings = models.ManyToManyField("self", blank=True)
    followers = models.ManyToManyField("self", blank=True)
    activation_code = models.CharField(max_length=100, default=1)
    nickname = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to=settings.MEDIA_ROOT + '/avatars', null=True, blank=True)
    objects = UserManager()

    def __str__(self):
        return "{}".format(self.username)