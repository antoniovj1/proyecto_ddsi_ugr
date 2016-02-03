from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from gestion_proveedores.models import *
from gestion_proveedores.forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required
def index(request):
    proveedores = Proveedor.objects.all()
    context = { 'proveedores' : proveedores}
    return render(request,'gestion_proveedores/index.html',context)


@login_required
def buscar(request):
    query = request.GET.get('search')

    if len(query) == 0:
        proveedores = Proveedor.objects.all()
        context = { 'proveedores' : proveedores}
        return render(request,'gestion_proveedores/index.html',context)
    else:
        proveedores = Proveedor.objects.filter(Q(nombre__contains=query) |
                                          Q(email__contains=query) |
                                          Q(telefono__contains=query) |
                                          Q(cod_postal__contains=query) |
                                          Q(localidad__contains=query) |
                                          Q(descripcion__contains=query) |
                                          Q(pais__contains=query) |
                                          Q(direccion__contains=query))
        context = { 'proveedores' : proveedores}
        return render(request,'gestion_proveedores/index.html',context)


@login_required
def altaProveedor(request):
    if request.method == "POST":
        form = AltaProveedorForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/proveedores')
    else:
        form = AltaProveedorForm()
    return render(request,'gestion_proveedores/alta_proveedor.html', {'form':form})

@login_required
def detallesProveedor(request ,id):
    proveedor = Proveedor.objects.get(pk = id)
    context = { 'proveedor' : proveedor }
    return render(request,'gestion_proveedores/detalles_proveedor.html',context)

@login_required
def eliminarProveedor(request, id):
    Proveedor.objects.get(pk = id).delete()
    return HttpResponseRedirect('/proveedores')

@login_required
def modificarProveedor(request, id):
        proveedor = Proveedor.objects.get(pk = id)

        if request.method == "POST":
            form = ModificarProveedorForm(request.POST,request.FILES)
            if form.is_valid():
                form = form.cleaned_data

                if(form['nombre']):
                    proveedor.nombre = form['nombre']
                if(form['email']):
                    proveedor.email = form['email']
                if(form['fax']):
                    proveedor.fax = form['fax']
                if(form['telefono']):
                    proveedor.telefono = form['telefono']
                if(form['localidad']):
                    proveedor.localidad = form['localidad']
                if(form['cod_postal']):
                    proveedor.cod_postal = form['cod_postal']
                if(form['direccion']):
                    proveedor.direccion = form['direccion']
                if(form['pais']):
                    proveedor.direccion = form['pais']
                if(form['descripcion']):
                    proveedor.direccion = form['descripcion']

                proveedor.save()

                return HttpResponseRedirect('/proveedores')
        else:
            form = ModificarProveedorForm(instance = proveedor)

        return render(request,'gestion_proveedores/modificar_proveedor.html', {'form':form})
