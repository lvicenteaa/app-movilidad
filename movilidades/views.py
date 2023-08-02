from django.shortcuts import render
from .models import Movilidad
from .forms import ModalidadForm, TipoForm, EventoForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='autenticacion')
def perfil(request):
    # movilidades = Movilidad.objects.get()
    # context = {
    #    'movilidades': movilidades
    # }
    return render(request, 'movilidades/authenticated/perfil.html')


@login_required(login_url='autenticacion')
def index(request):
    #movilidades = Movilidad.objects.get()
    #context = {
    #    'movilidades': movilidades
    #}
    #return render(request, 'movilidades/authenticated/index.html', context)
    return render(request, 'movilidades/authenticated/index.html')


@login_required(login_url='autenticacion')
def movilidades(request):
    if request.method == 'POST':
        # Guardar la información
        form = MovilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'movilidades/authenticated/movilidad.html', {'form': form})
    else:
        form = MovilidadForm()
        return render(request, 'movilidades/authenticated/movilidad.html', {'form': form})


login_required(login_url='autenticacion')
def tipos(request):
    if request.method == 'POST':
        # Guardar la información
        form = TipoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'movilidades/authenticated/tipo.html', {'form': form})
    else:
        form = TipoForm()
        return render(request, 'movilidades/authenticated/tipo.html', {'form': form})

login_required(login_url='autenticacion/')
def eventos(request):
    if request.method == 'POST':
        # Guardar la información
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'movilidades/authenticated/evento.html', {'form': form})
    else:
        form = EventoForm()
        return render(request, 'movilidades/authenticated/evento.html', {'form': form})

login_required(login_url='autenticacion/')
def modalidades(request):
    if request.method == 'POST':
        # Guardar la información
        form = ModalidadForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'movilidades/authenticated/modalidad.html', {'form': form})
    else:
        form = ModalidadForm()
        return render(request, 'movilidades/authenticated/modalidad.html', {'form': form})


