from django.db import models


class Imagen(models.Model):
    nombre = models.CharField(max_length=100, null=False, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'imagen'
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
        ordering = ['id']



