# Generated by Django 4.2.3 on 2023-07-21 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('codigo', models.CharField(max_length=7, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.CharField(max_length=255)),
                ('lugar', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True)),
                ('ciudad', models.CharField(max_length=255)),
                ('dependencia', models.CharField(max_length=255)),
                ('fecha_ida', models.DateField()),
                ('fecha_vuelta', models.DateField()),
                ('anio', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movilidades.usuario')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movilidades.evento')),
                ('modalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movilidades.modalidad')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movilidades.tipo')),
            ],
        ),
    ]
