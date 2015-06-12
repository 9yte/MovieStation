# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_auto_20150612_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to='/Mine/CE/Web Programming/Project/mysite/media/movie_covers', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='/Mine/CE/Web Programming/Project/mysite/media/avatars', null=True),
        ),
    ]
