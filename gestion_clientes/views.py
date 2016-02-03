from django.shortcuts import render
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
