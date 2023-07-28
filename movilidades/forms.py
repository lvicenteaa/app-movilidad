from django.forms import ModelForm
from .models import Tipo, Modalidad, Evento, Movilidad

class TipoForm(ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'
        
        
class ModalidadForm(ModelForm):
    class Meta:
        model = Modalidad
        fields = '__all__'
        
class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        
class MovilidadForm(ModelForm):
    class Meta:
        model = Movilidad
        fields = '__all__'