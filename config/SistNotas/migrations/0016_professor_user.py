# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-12 16:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SistNotas', '0015_auto_20180410_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
