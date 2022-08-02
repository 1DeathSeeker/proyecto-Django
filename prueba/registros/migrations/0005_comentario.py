# Generated by Django 4.0.5 on 2022-07-01 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0004_alumnos_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
                ('coment', models.TextField(verbose_name='Comentario')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.alumnos', verbose_name='Alumno')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'ordering': ['-created'],
            },
        ),
    ]
