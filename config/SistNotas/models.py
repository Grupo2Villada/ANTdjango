from django.db import models
from django.conf import settings
# Create your models here.

GRADE_CHOICES = (
    ('1', "Uno"),
    ('2', "Dos"),
    ('3', "Tres"),
    ('4', "Cuatro"),
    ('5', 'Cinco'),
    ('6', 'Seis'),
    ('7', 'Siete'),
    ('8', 'Ocho'),
    ('9', 'Nueve'),
    ('10', 'Diez'),
)
class Professor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)   
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        rta = self.first_name+" "+self.last_name
        return rta
        
class Student(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        rta = self.first_name+" "+self.last_name
        return rta

class Subject(models.Model):
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, blank=True)
    professors = models.ManyToManyField(Professor, blank=True)

    def __str__(self):
        return self.name
    
class Grade(models.Model):
    value = models.CharField(choices=GRADE_CHOICES, max_length= 2)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.value
