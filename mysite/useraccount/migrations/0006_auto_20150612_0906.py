# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0005_auto_20150612_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to='/Mine/CE/WebProgramming/Project/mysite/media/avatars', blank=True, null=True),
        ),
    ]
