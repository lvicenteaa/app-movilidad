from django.db import models


# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    codigo = models.CharField(unique=True, max_length=7)
    email = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.codigo


class Tipo(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Modalidad(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Movilidad(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    actividad = models.CharField(max_length=255)
    lugar = models.CharField(max_length=255)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    ciudad = models.CharField(max_length=255)
    dependencia = models.CharField(max_length=255)
    fecha_ida = models.DateField()
    fecha_vuelta = models.DateField()
    anio = models.IntegerField()
    semestre = models.IntegerField()

    def __str__(self):
        return self.actividad
