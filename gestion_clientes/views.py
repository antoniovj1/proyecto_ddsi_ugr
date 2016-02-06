from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from gestion_clientes.models import *
from gestion_clientes.forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required
def index(request):
    clientes = Cliente.objects.all()
    context = { 'clientes' : clientes}
    return render(request,'gestion_clientes/index.html',context)

@login_required
def buscar(request):
    query = request.GET.get('search')

    if len(query) == 0:
        clientes = Cliente.objects.all()
        context = { 'clientes' : clientes}
        return render(request,'gestion_clientes/index.html',context)
    else:
        clientes = Cliente.objects.filter(Q(nombre__contains=query) |
                                          Q(apellidos__contains=query) |
                                          Q(dni__contains=query) |
                                          Q(telefono__contains=query) |
                                          Q(cod_postal__contains=query) |
                                          Q(localidad__contains=query) |
                                          Q(direccion__contains=query))
        context = { 'clientes' : clientes}
        return render(request,'gestion_clientes/index.html',context)

@login_required
def altaCliente(request):
    if request.method == "POST":
        form = AltaClienteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/clientes')
    else:
        form = AltaClienteForm()

    return render(request,'gestion_clientes/alta_cliente.html', {'form':form})

@login_required
def detallesCliente(request ,id):
    cliente = Cliente.objects.get(pk = id)
    context = { 'cliente' : cliente }
    return render(request,'gestion_clientes/detalles_cliente.html',context)

@login_required
def eliminarCliente(request, id):
    Cliente.objects.get(pk = id).delete()
    return HttpResponseRedirect('/clientes')

@login_required
def modificarCliente(request, id):
        cliente = Cliente.objects.get(pk = id)

        if request.method == "POST":
            form = ModificarClienteForm(request.POST,request.FILES)
            if form.is_valid():
                form = form.cleaned_data

                if(form['foto']):
                    cliente.foto = form['foto']
                if(form['nombre']):
                    cliente.nombre = form['nombre']
                if(form['apellidos']):
                    cliente.apellidos = form['apellidos']
                if(form['f_nacimiento']):
                    cliente.f_nacimiento = form['f_nacimiento']
                if(form['telefono']):
                    cliente.telefono = form['telefono']
                if(form['localidad']):
                    cliente.localidad = form['localidad']
                if(form['cod_postal']):
                    cliente.cod_postal = form['cod_postal']
                if(form['direccion']):
                    cliente.direccion = form['direccion']
                if(form['sexo']):
                    cliente.sexo = form['sexo']

                cliente.save()

                return HttpResponseRedirect('/clientes')
        else:
            form = ModificarClienteForm(instance = cliente)
        return render(request,'gestion_clientes/modificar_cliente.html', {'form':form})

@login_required
def nuevaRevision(request,id):
    if request.method == "POST":
        form = RevisionForm(request.POST)

        cliente = Cliente.objects.get(pk = id)

        if form.is_valid() and cliente:
            form = form.cleaned_data

            revision = Revision()
            revision.cliente_rev = cliente

            if(form['descripcion']):
                revision.descripcion = form['descripcion']
            if(form['diagnostico']):
                revision.diagnostico = form['diagnostico']
            if(form['plan']):
                revision.plan = form['plan']
            if(form['oculista']):
                revision.oculista = form['oculista']
            if(form['fecha']):
                revision.fecha = form['fecha']

            revision.save()

            return HttpResponseRedirect(reverse('info_opto', args=[id]))
    else:
        form = RevisionForm()

    return render(request,'gestion_clientes/nueva_revision.html', {'form':form, 'cliente':id})


@login_required
def verResvisiones(request,id):
    revisiones = Revision.objects.filter(cliente_rev = id).order_by('fecha')
    context = { 'revisiones' : revisiones}
    context['id'] = id
    return render(request,'gestion_clientes/revisiones.html',context)

@login_required
def modificarRevision(request,id_rev):
    revision = Revision.objects.get(pk = id_rev)
    cliente = revision.cliente_rev
    cliente = cliente.id

    if request.method == "POST":
        form = RevisionForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data

            if(form['descripcion']):
                revision.descripcion = form['descripcion']
            if(form['diagnostico']):
                revision.diagnostico = form['diagnostico']
            if(form['plan']):
                revision.plan = form['plan']
            if(form['oculista']):
                revision.oculista = form['oculista']
            if(form['fecha']):
                revision.fecha = form['fecha']

            revision.save()

            return HttpResponseRedirect(reverse('info_opto', args=[cliente]))
    else:
        form = RevisionForm(instance = revision)
    return render(request,'gestion_clientes/modificar_revision.html', {'form':form, 'cliente':cliente})

@login_required
def detallesRevision(request,id_rev):
    revision = Revision.objects.get(pk = id_rev)
    cliente = revision.cliente_rev

    context = { 'cliente' : cliente }
    context['revision']=revision

    return render(request,'gestion_clientes/detalles_revision.html',context)

@login_required
def eliminarRevision(request, id_rev):
    rev = Revision.objects.get(pk = id_rev)

    cliente = rev.cliente_rev
    cliente = cliente.id

    rev.delete()
    return HttpResponseRedirect(reverse('info_opto', args=[cliente]))
