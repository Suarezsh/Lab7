from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/', views.cursos, name='cursos'),
    path('notas/', views.notas, name='notas'),

    path('agregar-alumno/', views.agregar_alumno, name='agregar_alumno'),
    path('eliminar-alumno/<str:idAlumno>/', views.eliminar_alumno, name='eliminar_alumno'),

    path('agregar-curso/', views.agregar_curso, name='agregar_curso'),
    path('eliminar-curso/<str:idCurso>/', views.eliminar_curso, name='eliminar_curso'),

    path('agregar-nota/', views.agregar_nota, name='agregar_nota'),
    path('eliminar-nota/<str:idNotasAlumnoPorCurso>/', views.eliminar_nota, name='eliminar_nota'),
]
