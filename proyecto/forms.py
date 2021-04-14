from django import forms
from .models import Cancha
from .models import Reserva

class CanchaForm(forms.ModelForm):

    class Meta:
        model = Cancha
        fields = ['cancha','codigoInterno','tipo','vestuarioDisponible','iluminacion','cespedSintetico']


class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ['cancha','cliente','empleado', 'fecha_reserva']
