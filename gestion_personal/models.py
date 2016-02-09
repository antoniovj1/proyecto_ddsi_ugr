from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Personal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')

    HOMBRE = 'Hombre'
    MUJER = 'Mujer'
    NONE = 'Sin especificar'
    OPCIONES = ((HOMBRE, 'Hombre'),
                (MUJER, 'Mujer'),
                (NONE, 'Sin especificar'),)

    nombre = models.CharField(max_length=20, blank=True)
    apellidos = models.CharField(max_length=20, blank=True)
    dni = models.CharField('DNI', max_length=9)
    f_nacimiento = models.DateField('Fecha de naciemiento', blank=True, null=True)
    direccion = models.CharField(max_length=30, blank=True)
    localidad = models.CharField(max_length=20, blank=True)
    cod_postal = models.CharField('Código postal', blank=True, null=True, max_length=5)
    telefono = models.CharField(blank=True, null=True, max_length=12)
    num_seg_social = models.CharField('Número seguridad social', max_length=12, blank=True, null=True)
    sexo = models.CharField(max_length=16, choices=OPCIONES, default=NONE)
    foto = models.ImageField(upload_to='personal/', null=True, blank=True)

    def delete(self, *args, **kwargs):
        # Preparamos las cosas antes de eliminar el objeto (guardamos la dirección de la foto)
        if self.foto:
            storage, path = self.foto.storage, self.foto.path
            # Primero eliminamos el objeto.
            super(Personal, self).delete(*args, **kwargs)
            # Despues eliminamos la foto
            storage.delete(path)
        else:
            super(Personal, self).delete(*args, **kwargs)
