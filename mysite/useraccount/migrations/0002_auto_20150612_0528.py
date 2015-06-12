# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='movie',
            name='cover_photo',
            field=models.ImageField(null=True, blank=True, upload_to='/Mine/CE/Web Programming/Project/mysite/images/movie_covers'),
        ),
    ]
