# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-05 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistNotas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='year',
            field=models.CharField(choices=[(b'1', b'1ero'), (b'2', b'2do'), (b'3', b'3ro'), (b'4', b'4to'), (b'5', b'5to'), (b'6', b'6to'), (b'7', b'7mo')], max_length=4),
        ),
    ]
