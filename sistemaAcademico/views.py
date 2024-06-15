from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Alumno, Curso, NotasAlumnoPorCurso
from .forms import AlumnoForm, CursoForm, NotasAlumnoPorCursoForm

def index(request):
    alumnos = Alumno.objects.all()
    return render(request, 'index.html', {'alumnos': alumnos})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def notas(request):
    notas = NotasAlumnoPorCurso.objects.select_related('alumno', 'curso').all()
    alumnos = Alumno.objects.all()
    cursos = Curso.objects.all()
    return render(request, 'notas.html', {'notas': notas, 'alumnos': alumnos, 'cursos': cursos})

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error'})

def eliminar_alumno(request, idAlumno):
    alumno = get_object_or_404(Alumno, idAlumno=idAlumno)
    if request.method == 'POST':
        alumno.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error'})

def eliminar_curso(request, idCurso):
    curso = get_object_or_404(Curso, idCurso=idCurso)
    if request.method == 'POST':
        curso.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def agregar_nota(request):
    if request.method == 'POST':
        form = NotasAlumnoPorCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error'})


def eliminar_nota(request, idNotasAlumnoPorCurso):
    nota = get_object_or_404(NotasAlumnoPorCurso, idNotasAlumnoPorCurso=idNotasAlumnoPorCurso)
    if request.method == 'POST':
        nota.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
