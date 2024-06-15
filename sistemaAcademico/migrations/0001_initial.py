# Generated by Django 5.0.6 on 2024-06-13 16:18

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('idAlumno', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('cui', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('idCurso', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('creditos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NotasAlumnoPorCurso',
            fields=[
                ('idNotasAlumnoPorCurso', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nota', models.DecimalField(decimal_places=2, max_digits=2)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistemaAcademico.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistemaAcademico.curso')),
            ],
        ),
    ]