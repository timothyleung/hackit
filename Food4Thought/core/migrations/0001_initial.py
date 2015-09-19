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
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.CharField(max_length=140)),
                ('info', models.CharField(max_length=200, blank=True)),
                ('where', models.CharField(max_length=140)),
                ('uid', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stars', models.IntegerField()),
                ('comment', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rid', models.ForeignKey(to='core.Request')),
                ('stateid', models.ForeignKey(to='core.State')),
                ('uid', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20, blank=True)),
                ('can_cook', models.BooleanField()),
                ('profile_picture', models.ImageField(upload_to=b'profile-pictures', blank=True)),
                ('rate', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='tid',
            field=models.ForeignKey(to='core.Transaction'),
        ),
        migrations.AddField(
            model_name='review',
            name='u1id',
            field=models.ForeignKey(related_name='u1id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='u2id',
            field=models.ForeignKey(related_name='u2id', to=settings.AUTH_USER_MODEL),
        ),
    ]
