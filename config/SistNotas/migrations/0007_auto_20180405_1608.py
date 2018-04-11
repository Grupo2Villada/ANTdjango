# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-05 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SistNotas', '0006_materia_profesores'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='id_materia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fk_materia', to='SistNotas.Materia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='materia',
            name='alumnos',
            field=models.ManyToManyField(blank=True, to='SistNotas.Alumno'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='profesores',
            field=models.ManyToManyField(blank=True, to='SistNotas.Profesor'),
        ),
    ]