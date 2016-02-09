from django.db import models


# Create your models here.

class Producto(models.Model):
    cantidad = models.PositiveIntegerField()
    codigo = models.CharField('Código', max_length=30, blank=True)
    nombre = models.CharField(max_length=30, blank=True)
    marca = models.CharField(max_length=30, blank=True)
    modelo = models.CharField(max_length=30, blank=True)
    precio = models.FloatField('Precio (EUR)')
    descripcion = models.TextField('Descripción', max_length=250, blank=True, null=True)
    foto = models.ImageField(upload_to='stock/', null=True, blank=True)

    def delete(self, *args, **kwargs):
        # Preparamos las cosas antes de eliminar el objeto (guardamos la dirección de la foto)
        if self.foto:
            storage, path = self.foto.storage, self.foto.path
            # Primero eliminamos el objeto.
            super(Producto, self).delete(*args, **kwargs)
            # Despues eliminamos la foto
            storage.delete(path)
        else:
            super(Producto, self).delete(*args, **kwargs)
