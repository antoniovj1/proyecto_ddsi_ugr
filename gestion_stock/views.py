from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

from gestion_stock.forms import *
from gestion_stock.models import Producto


# Create your views here.
@login_required
def index(request):
    """
    Índice gestión de stock
    :param request:
    :return:
    """
    productos = Producto.objects.all()
    context = {'productos': productos}

    return render(request, 'gestion_stock/index.html', context)


@login_required
def stock_bajo(request):
    """
    Muestra los productos con una cantifad menor o igual a 5.
    :param request:
    :return:
    """
    productos = Producto.objects.filter(cantidad__lte=5)
    context = {'productos': productos}
    return render(request, 'gestion_stock/index.html', context)


@login_required
def detalles_producto(request, id):
    """
    Muestra los detalles de un producto.
    :param request:
    :param id:
    :return:
    """
    producto = Producto.objects.get(pk=id)
    context = {'producto': producto}
    return render(request, 'gestion_stock/detalles_producto.html', context)


@login_required
def modificar_producto(request, id):
    """
    Modifica un producto.
    :param request:
    :param id:
    :return:
    """
    producto = Producto.objects.get(pk=id)

    if request.method == "POST":
        form = ModificarProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.cleaned_data

            if form['foto']:
                producto.foto = form['foto']
            if form['nombre']:
                producto.nombre = form['nombre']
            if form['codigo']:
                producto.codigo = form['codigo']
            if form['marca']:
                producto.marca = form['marca']
            if form['modelo']:
                producto.modelo = form['modelo']
            if form['precio']:
                producto.precio = form['precio']
            if form['descripcion']:
                producto.direccion = form['descripcion']

            producto.save()

            return HttpResponseRedirect('/stock')
    else:
        form = ModificarProductoForm(instance=producto)

    return render(request, 'gestion_stock/modificar_producto.html', {'form': form})


@login_required
def buscar(request):
    """
    Busca los productos que coinciden con query.
    :param request:
    :return:
    """
    query = request.GET.get('search')

    if len(query) == 0:
        productos = Producto.objects.all()
        context = {'productos': productos}
        return render(request, 'gestion_stock/index.html', context)
    else:
        productos = Producto.objects.filter(Q(codigo__contains=query) |
                                            Q(nombre__contains=query) |
                                            Q(marca__contains=query) |
                                            Q(modelo__contains=query) |
                                            Q(precio__contains=query) |
                                            Q(descripcion__contains=query))

        context = {'productos': productos}
        return render(request, 'gestion_stock/index.html', context)


@login_required
def nuevo_producto(request):
    """
    Añade un producto.
    :param request:
    :return:
    """
    if request.method == "POST":
        form = NuevoProductoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/stock')
    else:
        form = NuevoProductoForm()

    return render(request, 'gestion_stock/nuevo_producto.html', {'form': form})


@login_required
def eliminar_producto(request, id):
    """
    Elimina un producto.
    :param request:
    :param id:
    :return:
    """
    Producto.objects.get(pk=id).delete()
    return HttpResponseRedirect('/stock')


@login_required
def reponer_gastar_producto(request):
    """
    Esta función permite reponer un producto( número positivo ) o gastar
    una cantidad de un producto (número negativo). Además, cuando se gasta
    un producto PUEDE crear dos tipos de mensajes, uno advirtiendo que el
    producto pasa a estar en stock bajo (cantidad <=5) o que no se dispone
    de las suficientes unidades.
    :param request:
    :return:
    """
    productos = Producto.objects.all()
    cantidad = request.GET.get('cantidad')
    id = request.GET.get('id')

    cantidad = int(cantidad)
    id = int(id)

    mensaje = ''
    mensaje_stock = ''
    producto = Producto.objects.get(pk=id)

    if cantidad >= 0:
        producto.cantidad += cantidad
        producto.save()

    else:
        if abs(cantidad) > producto.cantidad:
            mensaje = 'No se dispone de tantos productos'
        else:
            producto.cantidad += cantidad  # Restamos la cantidad ( es negativo )
            producto.save()
            if Producto.objects.get(pk=id).cantidad <= 5:
                mensaje_stock = ("Stock bajo en el producto:" +
                                 "Código: " + str(Producto.objects.get(pk=id).codigo) +
                                 " Nombre: " + str(Producto.objects.get(pk=id).nombre))

    context = {'mensaje': mensaje, 'mensaje_stock': mensaje_stock, 'productos': productos}

    return render(request, 'gestion_stock/index.html', context)
