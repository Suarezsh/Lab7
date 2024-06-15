from django import forms
from .models import Alumno, Curso, NotasAlumnoPorCurso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['idAlumno', 'nombres', 'apellidos', 'cui']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['idCurso', 'nombre', 'creditos']

class NotasAlumnoPorCursoForm(forms.ModelForm):
    class Meta:
        model = NotasAlumnoPorCurso
        fields = ['idNotasAlumnoPorCurso', 'nota', 'alumno', 'curso']
