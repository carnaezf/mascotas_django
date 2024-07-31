from django.urls import path
from . import views  # Importamos las vistas desde la aplicación 'veterinarios'

urlpatterns = [
    path('agregar/', views.agregar_veterinario, name='agregar_veterinario'),
    path('lista/', views.lista_veterinarios, name='lista_veterinarios'),
]


