from django.shortcuts import render
from .models import Movilidad
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/autenticacion/logear')
def home(request):
    #movilidades = Movilidad.objects.get()
    #context = {
    #    'movilidades': movilidades
    #}
    return render(request, 'movilidades/perfil.html')

def movilidad(request):
    pass