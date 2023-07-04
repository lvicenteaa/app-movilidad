from django.db import models

# Create your models here.
class Actividad(models.Model):
    nombre = models.CharField(max_length=250, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre