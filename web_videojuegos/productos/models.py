from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length = 200, verbose_name="Titulo del Producto")
    descripcion = models.TextField(verbose_name = "Detalle del Producto")
    imagen = models.URLField(max_length = 200, verbose_name="Url de la imagen")
    precio = models.IntegerField(verbose_name="Precio del Producto", default=0)
    estaEnOferta = models.BooleanField(verbose_name="Está en oferta?", default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ["-titulo"]
    def __str__(self):
        return self.titulo