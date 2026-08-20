from django.shortcuts import redirect, render

from canciones.forms import CancionForm
from canciones.services.song_service import (
    crear_cancion, obtener_todas,)

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
