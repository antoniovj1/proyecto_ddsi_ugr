from django.db import models
from django.utils import timezone


# Create your models here.
class Cliente(models.Model):
    HOMBRE = 'Hombre'
    MUJER = 'Mujer'
    NONE = 'Sin especificar'
    OPCIONES = ((HOMBRE, 'Hombre'),
                (MUJER, 'Mujer'),
                (NONE, 'Sin especificar'),)

    nombre = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    dni = models.CharField('DNI', max_length=9)  # Mejorar
    f_nacimiento = models.DateField('Fecha de naciemiento', blank=True, null=True)
    direccion = models.CharField('Dirección', max_length=30, blank=True)
    localidad = models.CharField(max_length=20, blank=True)
    cod_postal = models.CharField('Código postal', blank=True, null=True, max_length=5)
    telefono = models.CharField(blank=True, null=True, max_length=12)
    sexo = models.CharField(max_length=16, choices=OPCIONES, default=NONE)
    foto = models.ImageField(upload_to='clientes/', null=True, blank=True)

    def delete(self, *args, **kwargs):
        # Preparamos las cosas antes de eliminar el objeto (guardamos la dirección de la foto)
        if self.foto:
            storage, path = self.foto.storage, self.foto.path
            # Primero eliminamos el objeto.
            super(Cliente, self).delete(*args, **kwargs)
            # Despues eliminamos la foto
            storage.delete(path)
        else:
            super(Cliente, self).delete(*args, **kwargs)


class Revision(models.Model):
    cliente_rev = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    fecha = models.DateField(default=timezone.now, blank=True)
    descripcion = models.TextField('Descripción', blank=True, null=True, max_length=150)
    diagnostico = models.TextField('Diagnóstico', blank=True, null=True, max_length=150)
    plan = models.TextField(blank=True, null=True, max_length=150)
    oculista = models.CharField(blank=True, null=True, max_length=50)
