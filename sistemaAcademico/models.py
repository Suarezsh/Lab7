from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Alumno(models.Model):
    idAlumno = models.CharField(max_length=32, primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cui = models.IntegerField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Curso(models.Model):
    idCurso = models.CharField(max_length=32, primary_key=True)
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField()

    def __str__(self):
        return self.nombre

class NotasAlumnoPorCurso(models.Model):
    idNotasAlumnoPorCurso = models.CharField(max_length=32, primary_key=True)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notas de {self.alumno.nombres} en {self.curso.nombre}"
