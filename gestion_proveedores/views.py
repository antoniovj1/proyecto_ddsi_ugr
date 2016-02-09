from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

from gestion_proveedores.forms import *
from gestion_proveedores.models import *


# Create your views here.
@login_required
def index(request):
    """
    Índice gestión de proveedores.
    :param request:
    :return:
    """
    proveedores = Proveedor.objects.all()
    context = {'proveedores': proveedores}
    return render(request, 'gestion_proveedores/index.html', context)


@login_required
def buscar(request):
    """
    Busca los proveedores que coincidan con query
    :param request:
    :return:
    """
    query = request.GET.get('search')

    if len(query) == 0:
        proveedores = Proveedor.objects.all()
        context = {'proveedores': proveedores}
        return render(request, 'gestion_proveedores/index.html', context)
    else:
        proveedores = Proveedor.objects.filter(Q(nombre__contains=query) |
                                               Q(email__contains=query) |
                                               Q(telefono__contains=query) |
                                               Q(cod_postal__contains=query) |
                                               Q(localidad__contains=query) |
                                               Q(descripcion__contains=query) |
                                               Q(pais__contains=query) |
                                               Q(direccion__contains=query))
        context = {'proveedores': proveedores}
        return render(request, 'gestion_proveedores/index.html', context)


@login_required
def alta_proveedor(request):
    """
    Añade un proveedor.
    :param request:
    :return:
    """
    if request.method == "POST":
        form = AltaProveedorForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/proveedores')
    else:
        form = AltaProveedorForm()
    return render(request, 'gestion_proveedores/alta_proveedor.html', {'form': form})


@login_required
def detalles_proveedor(request, id):
    """
    Muestra los detalles de un proveedor.
    :param request:
    :param id:
    :return:
    """
    proveedor = Proveedor.objects.get(pk=id)
    context = {'proveedor': proveedor}
    return render(request, 'gestion_proveedores/detalles_proveedor.html', context)


@login_required
def eliminar_proveedor(request, id):
    """
    Elimina un proveedor.
    :param request:
    :param id:
    :return:
    """
    Proveedor.objects.get(pk=id).delete()
    return HttpResponseRedirect('/proveedores')


@login_required
def modificar_proveedor(request, id):
    """
    Modifica un proveedor.
    :param request:
    :param id:
    :return:
    """
    proveedor = Proveedor.objects.get(pk=id)

    if request.method == "POST":
        form = ModificarProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.cleaned_data

            if form['foto']:
                proveedor.foto = form['foto']
            if form['nombre']:
                proveedor.nombre = form['nombre']
            if form['email']:
                proveedor.email = form['email']
            if form['fax']:
                proveedor.fax = form['fax']
            if form['telefono']:
                proveedor.telefono = form['telefono']
            if form['localidad']:
                proveedor.localidad = form['localidad']
            if form['cod_postal']:
                proveedor.cod_postal = form['cod_postal']
            if form['direccion']:
                proveedor.direccion = form['direccion']
            if form['pais']:
                proveedor.direccion = form['pais']
            if form['descripcion']:
                proveedor.direccion = form['descripcion']

            proveedor.save()

            return HttpResponseRedirect('/proveedores')
    else:
        form = ModificarProveedorForm(instance=proveedor)

    return render(request, 'gestion_proveedores/modificar_proveedor.html', {'form': form})
