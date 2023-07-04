from django.shortcuts import render
from .forms import ActividadForm

# Create your views here.
def index(request):
    form = ActividadForm()
    return render(request, 'index.html', {'form': form})