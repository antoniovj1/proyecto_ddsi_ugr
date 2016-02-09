from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

from gestion_clientes.forms import *
from gestion_clientes.models import *


# Create your views here.
@login_required
def index(request):
    """
    Índice de gestión clientes.
    :param request:
    :return:
    """
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'gestion_clientes/index.html', context)


@login_required
def buscar(request):
    """
    Busca los clientes que coincidan con query.
    :param request:
    :return:
    """
    query = request.GET.get('search')

    if len(query) == 0:
        clientes = Cliente.objects.all()
        context = {'clientes': clientes}
        return render(request, 'gestion_clientes/index.html', context)
    else:
        clientes = Cliente.objects.filter(Q(nombre__contains=query) |
                                          Q(apellidos__contains=query) |
                                          Q(dni__contains=query) |
                                          Q(telefono__contains=query) |
                                          Q(cod_postal__contains=query) |
                                          Q(localidad__contains=query) |
                                          Q(direccion__contains=query))
        context = {'clientes': clientes}
        return render(request, 'gestion_clientes/index.html', context)


@login_required
def alta_cliente(request):
    """
    Añade un nuevo cliente.
    :param request:
    :return:
    """
    if request.method == "POST":
        form = AltaClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/clientes')
    else:
        form = AltaClienteForm()

    return render(request, 'gestion_clientes/alta_cliente.html', {'form': form})


@login_required
def detalles_cliente(request, id):
    """
    Muestra un cliente en detalle.
    :param request:
    :param id:
    :return:
    """
    cliente = Cliente.objects.get(pk=id)
    context = {'cliente': cliente}
    return render(request, 'gestion_clientes/detalles_cliente.html', context)


@login_required
def eliminar_cliente(request, id):
    """
    Elimina un cliente.
    :param request:
    :param id:
    :return:
    """
    Cliente.objects.get(pk=id).delete()
    return HttpResponseRedirect('/clientes')


@login_required
def modificar_cliente(request, id):
    """
    Modifica a un cliente.
    :param request:
    :param id:
    :return:
    """
    cliente = Cliente.objects.get(pk=id)

    if request.method == "POST":
        form = ModificarClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.cleaned_data

            if form['foto']:
                cliente.foto = form['foto']
            if form['nombre']:
                cliente.nombre = form['nombre']
            if form['apellidos']:
                cliente.apellidos = form['apellidos']
            if form['f_nacimiento']:
                cliente.f_nacimiento = form['f_nacimiento']
            if form['telefono']:
                cliente.telefono = form['telefono']
            if form['localidad']:
                cliente.localidad = form['localidad']
            if form['cod_postal']:
                cliente.cod_postal = form['cod_postal']
            if form['direccion']:
                cliente.direccion = form['direccion']
            if form['sexo']:
                cliente.sexo = form['sexo']

            cliente.save()

            return HttpResponseRedirect('/clientes')
    else:
        form = ModificarClienteForm(instance=cliente)
    return render(request, 'gestion_clientes/modificar_cliente.html', {'form': form})


@login_required
def nueva_revision(request, id):
    """
    Añade una revisión para un cliente.
    :param request:
    :param id: ID del cliente.
    :return:
    """
    if request.method == "POST":
        form = RevisionForm(request.POST)

        cliente = Cliente.objects.get(pk=id)

        if form.is_valid() and cliente:
            form = form.cleaned_data

            revision = Revision()
            revision.cliente_rev = cliente

            if form['descripcion']:
                revision.descripcion = form['descripcion']
            if form['diagnostico']:
                revision.diagnostico = form['diagnostico']
            if form['plan']:
                revision.plan = form['plan']
            if form['oculista']:
                revision.oculista = form['oculista']
            if form['fecha']:
                revision.fecha = form['fecha']

            revision.save()

            return HttpResponseRedirect(reverse('info_opto', args=[id]))
    else:
        form = RevisionForm()

    return render(request, 'gestion_clientes/nueva_revision.html', {'form': form, 'cliente': id})


@login_required
def ver_resvisiones(request, id):
    """
    Muestra las revisiones de un cliente.
    :param request:
    :param id: ID del cliente
    :return:
    """
    revisiones = Revision.objects.filter(cliente_rev=id).order_by('fecha')
    context = {'revisiones': revisiones, 'id': id}
    return render(request, 'gestion_clientes/revisiones.html', context)


@login_required
def modificar_revision(request, id_rev):
    """
    Modifica un revisión.
    :param request:
    :param id_rev:
    :return:
    """
    revision = Revision.objects.get(pk=id_rev)
    cliente = revision.cliente_rev
    cliente = cliente.id

    if request.method == "POST":
        form = RevisionForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data

            if form['descripcion']:
                revision.descripcion = form['descripcion']
            if form['diagnostico']:
                revision.diagnostico = form['diagnostico']
            if form['plan']:
                revision.plan = form['plan']
            if form['oculista']:
                revision.oculista = form['oculista']
            if form['fecha']:
                revision.fecha = form['fecha']

            revision.save()

            return HttpResponseRedirect(reverse('info_opto', args=[cliente]))
    else:
        form = RevisionForm(instance=revision)
    return render(request, 'gestion_clientes/modificar_revision.html', {'form': form, 'cliente': cliente})


@login_required
def detalles_revision(request, id_rev):
    """
    Muestra los detalles de una revisón.
    :param request:
    :param id_rev:
    :return:
    """
    revision = Revision.objects.get(pk=id_rev)
    cliente = revision.cliente_rev

    context = {'cliente': cliente, 'revision': revision}

    return render(request, 'gestion_clientes/detalles_revision.html', context)


@login_required
def eliminar_revision(request, id_rev):
    """
    Elimina una revisión.
    :param request:
    :param id_rev:
    :return:
    """
    rev = Revision.objects.get(pk=id_rev)

    cliente = rev.cliente_rev
    cliente = cliente.id

    rev.delete()
    return HttpResponseRedirect(reverse('info_opto', args=[cliente]))
