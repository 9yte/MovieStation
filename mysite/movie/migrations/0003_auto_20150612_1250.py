# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20150612_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover_photo',
            field=models.ImageField(null=True, upload_to='/movie_covers', blank=True),
        ),
    ]
