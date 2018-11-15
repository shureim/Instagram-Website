# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-13 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_auto_20181112_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='user',
        ),
        migrations.AddField(
            model_name='likes',
            name='like',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='likes',
            name='postid',
            field=models.IntegerField(null=True),
        ),
    ]