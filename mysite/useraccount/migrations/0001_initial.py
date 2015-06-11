# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings
import django.utils.timezone
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='username', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('activation_code', models.CharField(max_length=100, default=1)),
                ('nickname', models.CharField(max_length=20, blank=True, null=True)),
                ('avatar', models.ImageField(upload_to='/Mine/CE/Web Programming/Project/mysite/images/avatars', blank=True, null=True)),
                ('followers', models.ManyToManyField(related_name='followers_rel_+', to=settings.AUTH_USER_MODEL)),
                ('followings', models.ManyToManyField(related_name='followings_rel_+', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', verbose_name='groups', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True)),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', verbose_name='user permissions', to='auth.Permission', help_text='Specific permissions for this user.', blank=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('text', models.CharField(max_length=350)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True)),
                ('IMDB_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to='/Mine/CE/Web Programming/Project/mysite/images/post_images')),
                ('rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('text', models.TextField(blank=True)),
                ('date', models.DateField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(to='useraccount.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='favourite',
            name='post',
            field=models.ForeignKey(to='useraccount.Post'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='useraccount.Post'),
        ),
    ]
