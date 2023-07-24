from django.shortcuts import render, redirect
from .models import Proyecto
from .forms import ProyectoForm
from django.contrib import messages

# Create your views here.
def index(request):
    proyectos = Proyecto.objects.get()
    return render(request, 'proyectos/proyectos_list.html', {'proyectos': proyectos})

def view(request, id):
    proyecto = Proyecto.objects.get(id=id)
    context = {
        'proyecto': proyecto
    }
    return render(request, 'proyectos/proyectos.html', context)

def edit(request, id):
    proyecto = Proyecto.objects.get(id=id)
    if request.method =='GET':
        form = ProyectoForm(instance=proyecto)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'proyectos/edit.html', context)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'id': id
            }
        messages.sucess(request, 'Proyecto actualizado')
        return render(request, 'proyecto/edit.html', context)

def create(request):
    if request.method == 'GET':
        form = ProyectoForm()
        context = {
            'form': 'form'
        }
        return render(request, 'proyecto/create.html', context)
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contact')

def delete(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect('proyecto')