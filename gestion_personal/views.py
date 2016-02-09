from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

from gestion_personal.forms import UserForm, AltaPersonalForm, ModificarPersonalForm
from gestion_personal.models import *


# Create your views here.
@login_required
def index(request):
    """
    Índice gestión de personal.
    :param request:
    :return:
    """
    personal = Personal.objects.all()
    context = {'personal': personal}
    return render(request, 'gestion_personal/index.html', context)


@login_required
def buscar(request):
    """
    Muestra los empleados que coincidan con query.
    :param request:
    :return:
    """
    query = request.GET.get('search')

    if len(query) == 0:
        personal = Personal.objects.all()
        context = {'personal': personal}
        return render(request, 'gestion_personal/index.html', context)
    else:
        personal = Personal.objects.filter(Q(nombre__contains=query) |
                                           Q(apellidos__contains=query) |
                                           Q(dni__contains=query) |
                                           Q(telefono__contains=query) |
                                           Q(cod_postal__contains=query) |
                                           Q(localidad__contains=query) |
                                           Q(num_seg_social__contains=query) |
                                           Q(direccion__contains=query))
        context = {'personal': personal}
        return render(request, 'gestion_personal/index.html', context)


@login_required
def alta_personal(request):
    """
    Añade un empleado.
    :param request:
    :return:
    """
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        personal_form = AltaPersonalForm(request.POST)

        if user_form.is_valid() and personal_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = personal_form.save(commit=False)
            profile.user = user

            profile.save()
            return HttpResponseRedirect('/personal')
    else:
        user_form = UserForm()
        personal_form = AltaPersonalForm()

    return render(request, 'gestion_personal/alta_personal.html',
                  {'user_form': user_form, 'personal_form': personal_form})


@login_required
def detalles_personal(request, id):
    """
    Muestra los detalles de un empleado.
    :param request:
    :param id:
    :return:
    """
    personal = Personal.objects.get(pk=id)
    context = {'personal': personal}
    return render(request, 'gestion_personal/detalles_personal.html', context)


@login_required
def eliminar_personal(request, id):
    """
    Elimina un empleado.
    :param request:
    :param id:
    :return:
    """
    Personal.objects.get(pk=id).user.delete()
    return HttpResponseRedirect('/personal')


@login_required
def modificar_personal(request, id):
    """
    Modifica a un empleado.
    :param request:
    :param id:
    :return:
    """
    personal = Personal.objects.get(pk=id)

    if request.method == "POST":
        form = ModificarPersonalForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.cleaned_data

            if form['foto']:
                personal.foto = form['foto']
            if form['nombre']:
                personal.nombre = form['nombre']
            if form['apellidos']:
                personal.apellidos = form['apellidos']
            if form['f_nacimiento']:
                personal.f_nacimiento = form['f_nacimiento']
            if form['telefono']:
                personal.telefono = form['telefono']
            if form['localidad']:
                personal.localidad = form['localidad']
            if form['cod_postal']:
                personal.cod_postal = form['cod_postal']
            if form['direccion']:
                personal.direccion = form['direccion']
            if form['sexo']:
                personal.sexo = form['sexo']

            personal.save()

            return HttpResponseRedirect('/personal')

    else:
        form = ModificarPersonalForm(instance=personal)

    return render(request, 'gestion_personal/modificar_personal.html', {'form': form})
