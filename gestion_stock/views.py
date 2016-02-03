from django.shortcuts import render
from gestion_stock.models import Producto
from gestion_stock.forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


# Create your views here.
@login_required
def index(request):
    productos = Producto.objects.all()
    context = { 'productos' : productos }

    return render(request,'gestion_stock/index.html',context)

@login_required
def stockBajo(request):
    productos = Producto.objects.filter(cantidad__lte = 5)
    context = { 'productos' : productos}
    return render(request,'gestion_stock/index.html',context)

@login_required
def detallesProducto(request ,id):
    producto = Producto.objects.get(pk = id)
    context = { 'producto' : producto }
    return render(request,'gestion_stock/detalles_producto.html',context)

@login_required
def modificarProducto(request, id):
        producto = Producto.objects.get(pk = id)

        if request.method == "POST":
            form = ModificarProductoForm(request.POST,request.FILES)
            if form.is_valid():
                form = form.cleaned_data

                if(form['nombre']):
                    producto.nombre = form['nombre']
                if(form['codigo']):
                    producto.codigo = form['codigo']
                if(form['marca']):
                    producto.marca = form['marca']
                if(form['modelo']):
                    producto.modelo = form['modelo']
                if(form['precio']):
                    producto.precio = form['precio']
                if(form['descripcion']):
                    producto.direccion = form['descripcion']

                producto.save()

                return HttpResponseRedirect('/stock')
        else:
            form = ModificarProductoForm(instance = producto)

        return render(request,'gestion_stock/modificar_producto.html', {'form':form})



@login_required
def buscar(request):
    query = request.GET.get('search')

    if len(query) == 0:
        productos = Producto.objects.all()
        context = { 'productos' : productos}
        return render(request,'gestion_stock/index.html',context)
    else:
        productos = Producto.objects.filter(Q(codigo__contains=query) |
                                          Q(nombre__contains=query) |
                                          Q(marca__contains=query) |
                                          Q(modelo__contains=query) |
                                          Q(precio__contains=query) |
                                          Q(descripcion__contains=query))

        context = { 'productos' : productos}
        return render(request,'gestion_stock/index.html',context)



@login_required
def nuevoProducto(request):
    if request.method == "POST":
        form = NuevoProductoForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/stock')
    else:
        form = NuevoProductoForm()

    return render(request,'gestion_stock/nuevo_producto.html', {'form':form})

@login_required
def eliminarProducto(request, id):
    Producto.objects.get(pk=id).delete()
    return HttpResponseRedirect('/stock')

@login_required
def reponerGastarProducto(request):
    productos = Producto.objects.all()
    cantidad = request.GET.get('cantidad')
    id = request.GET.get('id')

    cantidad = int(cantidad)
    id = int(id)

    mensaje = ''
    mensaje_stock = ''
    producto = Producto.objects.get(pk=id)

    if cantidad >= 0:
        producto.cantidad+=cantidad
        producto.save()

    else:
        if abs(cantidad) > producto.cantidad:
            mensaje = 'No se dispone de tantos productos'
        else:
            producto.cantidad+=cantidad # Restamos la cantidad ( es negativo )
            producto.save()
            if Producto.objects.get(pk=id).cantidad < 5:
                mensaje_stock = ("Stock bajo en el producto:" +
                                "Código: " + str(Producto.objects.get(pk=id).codigo) +
                               " Nombre: " + str(Producto.objects.get(pk=id).nombre))

    context = {}
    context['mensaje'] = mensaje
    context['mensaje_stock'] = mensaje_stock
    context['productos'] = productos

    return render(request,'gestion_stock/index.html',context)
