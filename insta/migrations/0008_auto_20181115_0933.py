# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-15 06:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0007_auto_20181114_1931'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Likes',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
