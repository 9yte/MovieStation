# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0003_auto_20150612_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers_rel_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='followings',
            field=models.ManyToManyField(blank=True, related_name='followings_rel_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
