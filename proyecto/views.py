from django.shortcuts import render, redirect
from .models import Cancha
from .forms import CanchaForm
from .models import Reserva
from .forms import ReservaForm
from django.core.paginator import Paginator
from django.http import Http404

def home(request):
    canchas = Cancha.objects.all()
    context = {'canchas':canchas}
    return render(request, 'proyecto/home.html', context)

def agregar(request):
    if request.method == 'POST':
        form = CanchaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CanchaForm()

    context = {'form':form}
    return render(request, 'proyecto/agregar.html', context)

def eliminar(request, cancha_id):
    cancha = Cancha.objects.get(id=cancha_id)
    cancha.delete()
    return redirect('home')

def editar(request, cancha_id):
    cancha = Cancha.objects.get(id=cancha_id)
    if request.method == 'POST':
        form = CanchaForm(request.POST, instance=cancha)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CanchaForm(instance=cancha)

    context = {'form':form}
    return render(request, 'proyecto/editar.html', context)






def listaReserva(request):
    reservas = Reserva.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator =  Paginator(reservas, 20)
        reservas = paginator.page(page)
    except:
        raise Http404

    context = {'reservas':reservas}

    return render(request, 'proyecto/listaReserva.html', context)

def agregarReserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaReserva')
    else:
        form = ReservaForm()

    context = {'form':form}
    return render(request, 'proyecto/agregarReserva.html', context)

def eliminarReserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    reserva.delete()
    return redirect('listaReserva')


def editarReserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('listaReserva')
    else:
        form = ReservaForm(instance=reserva)

    context = {'form':form}
    return render(request, 'proyecto/editarReserva.html', context)





