# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-10 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistNotas', '0013_auto_20180410_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='value',
            field=models.BooleanField(choices=[(b'1', b'Uno'), (b'2', b'Dos')], max_length=2),
        ),
    ]
