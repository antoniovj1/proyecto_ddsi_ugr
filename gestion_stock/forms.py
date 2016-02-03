from django.forms import ModelForm
from django import forms
from gestion_stock.models import Producto


class NuevoProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['foto','cantidad','codigo','nombre','marca','modelo',
                  'precio','descripcion']


class ModificarProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['foto','codigo','nombre','marca','modelo',
                  'precio','descripcion']
