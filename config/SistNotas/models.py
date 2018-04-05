from django.db import models
from django.conf import settings
# Create your models here.

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

    def __str__(self):
        rta = self.nombre+" "+self.apellido
        return rta
        
class Alumno(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        rta = self.nombre+" "+self.apellido
        return rta

class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    alumnos = models.ManyToManyField(Alumno, blank=True)
    profesores = models.ManyToManyField(Profesor, blank=True)

    def __str__(self):
        return self.nombre
    
class Nota(models.Model):
    valor = models.CharField(choices=NOTAS_CHOICES, max_length= 2)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='fk_materia')
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='fk_alumno')

    def __str__(self):
        return self.valor
