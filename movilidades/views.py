from django.shortcuts import render
from .models import Movilidad

# Create your views here.
def home(request):
    movilidades = Movilidad.objects.get()
    context = {
        'movilidades': movilidades
    }
    return render(request, 'movilidades/index.html', context)