from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import EquipoForm

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            total = datos['membresia'] * datos['cantidad']
            datos['total'] = total
            return render(request, 'equipo_exito.html', {'datos': datos})
    else:
        inicial = {
            'nombre_equipo': '',
            'nombre_jefe': '',
            'membresia': '',
            'cantidad': '',
        }
        form = EquipoForm(initial=inicial)
    
    return render(request, 'equipo_formulario.html', {'form': form})