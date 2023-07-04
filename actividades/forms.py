from django.forms import ModelForm
from .models import Actividad

class ActividadForm(ModelForm):
    class Meta:
        model= Actividad
        fields= "__all__"