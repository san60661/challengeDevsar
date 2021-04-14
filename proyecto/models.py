from django.db import models
from datetime import datetime, date

# Create your models here.

from django.db import models

# Create your models here.

class Cancha(models.Model):
    cancha = models.CharField(max_length=80)
    codigoInterno = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    vestuarioDisponible = models.BooleanField()
    iluminacion = models.BooleanField()
    cespedSintetico = models.BooleanField()


    def __str__(self):
        return self.cancha

class Reserva(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=50)
    empleado = models.CharField(max_length=50)
    fecha_reserva = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    #fechaR = models.DateField(auto_now_add=True, auto_now=False, blank=True)
