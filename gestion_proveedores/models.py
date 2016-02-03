from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=30,blank=True)
    email = models.CharField(max_length=30,blank=True)
    direccion = models.CharField(max_length=30,blank=True)
    localidad = models.CharField(max_length=20,blank=True)
    pais = models.CharField(max_length=20,blank=True)
    cod_postal = models.CharField('Código postal',blank=True,null=True,max_length=5)
    telefono = models.CharField(blank=True,null=True,max_length=12)
    fax = models.CharField(blank=True,null=True,max_length=9)
    descripcion = models.TextField(max_length=250,blank=True,null=True)
    foto = models.ImageField(upload_to='proveedores/', null = True,blank=True)

    def delete(self, *args, **kwargs):
        # Preparamos las cosas antes de eliminar el objeto (guardamos la dirección de la foto)
        if(self.foto):
            storage, path = self.foto.storage, self.foto.path
            # Primero eliminamos el objeto.
            super(Proveedor, self).delete(*args, **kwargs)
            # Despues eliminamos la foto
            storage.delete(path)
        else:
            super(Proveedor, self).delete(*args, **kwargs)
