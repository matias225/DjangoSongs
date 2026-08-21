from django.shortcuts import get_object_or_404, redirect, render
from canciones.models import Cancion

from canciones.forms import CancionForm
from canciones.services.song_service import (
    actualizar_cancion,
    crear_cancion,
    eliminar_cancion,
    obtener_todas,
)

def index(request):
    canciones = obtener_todas()
    context = { 'canciones': canciones }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            crear_cancion(form.cleaned_data)
            return redirect('index')
    else:
        form = CancionForm()

    context = { 'form': form }
    return render(request, 'canciones/form.html', context)

def update(request, id):
    cancion = get_object_or_404(Cancion, id=id)

    if request.method == 'POST':
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            actualizar_cancion(id, form.cleaned_data)
            return redirect('index')
    else:
        form = CancionForm(instance=cancion)

    context = {'form': form, 'cancion': cancion,}
    return render(request, 'canciones/form.html', context)

def delete(request, id):

    if request.method == 'POST':
        cancion = get_object_or_404(Cancion,id=id)
        eliminar_cancion(id)

        return redirect('index')
    return redirect('index')
