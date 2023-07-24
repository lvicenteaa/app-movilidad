from django.forms import ModelForm
from .models import Proyecto

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        exclude = ('date',)