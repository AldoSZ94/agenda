from django.db import models


class Tarea(models.Model):

    class Prioridades(models.TextChoices):
        BAJA = "baja", "Baja"
        MEDIA = "media", "Media"
        ALTA = "alta", "Alta"

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    prioridad = models.CharField(
        max_length=10, choices=Prioridades.choices, default=Prioridades.BAJA
    )
    fecha_creada = models.DateField(auto_now_add=True)
    fecha_actualizada = models.DateField(auto_now=True)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
