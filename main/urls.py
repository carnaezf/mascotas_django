from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('saludo/<str:nombre>/', views.saludo, name='saludo'),
    path('mascotas/', views.mascotas, name='mascotas'),
    path('detalle_mascota/<str:nombre>/', views.detalle_mascota, name='detalle_mascota'),
    path('agregar/', views.agregar_mascota, name='agregar_mascota'),
    path('lista/', views.lista_mascotas, name='lista_mascotas'),

]
