from django.db import models

# Create your models here.
class TipoProyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    director = models.CharField(max_length=255)
    fecha_inicio = models.DateTimeField()
    estado = models.CharField(max_length=255)
    created_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class EstadoProyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre