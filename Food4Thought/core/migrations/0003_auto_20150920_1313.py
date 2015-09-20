# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150920_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='where',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='request',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='lon',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
