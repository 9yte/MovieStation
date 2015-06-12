# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True)),
                ('IMDB_link', models.CharField(max_length=100)),
                ('cover_photo', models.ImageField(upload_to='/Mine/CE/Web Programming/Project/mysite/media/movie_covers', blank=True, null=True)),
            ],
        ),
    ]
