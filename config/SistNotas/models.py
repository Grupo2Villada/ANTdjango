from django.db import models

# Create your models here.

DIVISION_CHOICES = (
    ('A', 'a'),
    ('B', 'b'),
    ('C', 'c'),
)

YEAR_CHOICES = (
    ('1', '1°'),
    ('2', '2°'),
    ('3', '3°'),
    ('4', '4°'),
    ('5', '5°'),
    ('6', '6°'),
    ('7', '7°'),
)

NOTAS_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)
class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)

class Curso(models.Model):
    year = models.IntegerField(choices=YEAR_CHOICES)
    division = models.CharField(choices=DIVISION_CHOICES)
    id_profesor = models.ForeignKeyField(Profesor, on_delete=models.CASCADE, related_name='fk_profesor')

class Nota(models.Model):
    valor = models.IntegerField(choices=NOTAS_CHOICES)
    id_alumno = models.ForeignKeyField(Alumno, on_delete=models.CASCADE, related_name='fk_alumno')

class Alumno(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    id_curso = models.ForeignKeyField(Curso, on_delete=models.CASCADE, related_name='fk_curso')
    
