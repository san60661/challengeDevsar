from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('agregar/', views.agregar, name='agregar'),

    path('eliminar/<cancha_id>/', views.eliminar, name='eliminar'),

    path('editar/<cancha_id>/', views.editar, name='editar'),



    path('listaReserva', views.listaReserva, name='listaReserva'),

    path('agregarReserva/', views.agregarReserva, name='agregarReserva'),

    path('eliminarReserva/<reserva_id>/', views.eliminarReserva, name='eliminarReserva'),

    path('editarReserva/<reserva_id>/', views.editarReserva, name='editarReserva'),

]
