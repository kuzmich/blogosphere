# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='read',
            new_name='read_by',
        ),
        migrations.AlterField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(to='blog.Blog', related_name='posts'),
            preserve_default=True,
        ),
    ]
