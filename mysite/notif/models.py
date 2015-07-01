from django.db import models


class Notif(models.Model):
    user = models.ForeignKey('useraccount.UserProfile')
    url = models.CharField(max_length=50)
    date_time = models.DateTimeField(blank=False, null=False)
    text = models.CharField(max_length=80)

    def __str__(self):
        return "{}".format(self.text)