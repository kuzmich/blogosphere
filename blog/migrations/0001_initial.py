# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('subscribers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='subscriptions')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('text', models.TextField(verbose_name='содержание')),
                ('created', models.DateTimeField(verbose_name='создан', auto_now_add=True)),
                ('blog', models.ForeignKey(to='blog.Blog')),
                ('read', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='read_posts')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
