from django.contrib import admin

# Register your models here.
from .models import Alumno
from .models import Curso
from .models import NotasAlumnoPorCurso

admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(NotasAlumnoPorCurso)