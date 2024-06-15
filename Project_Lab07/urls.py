# Project_Lab07/urls.py

from django.contrib import admin
from django.urls import path, include  # Importa include aquí
from sistemaAcademico.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('sistema/', include('sistemaAcademico.urls')),  # Usa include para incluir las URLs de sistemaAcademico
]
