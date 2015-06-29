from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings


class UserProfile(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    followings = models.ManyToManyField("self", blank=True)
    followers = models.ManyToManyField("self", blank=True)
    #followings = models.ManyToManyField("self", through='FollowRelation', symmetrical=False)
    #followers = models.ManyToManyField("self", through='FollowRelation', related_name="users_following_user")
    activation_code = models.CharField(max_length=100, default=1)
    nickname = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    objects = UserManager()

    def __str__(self):
        return "{}".format(self.username)


#class FollowRelation(models.Model):
#    followerUser = models.ForeignKey(UserProfile, related_name="user_following")
#    followedUser = models.ForeignKey(UserProfile, related_name="user_followed")
#
#    def __str__(self):
#        return "%s following %s" % self.followerUser.name, self.followedUser.name