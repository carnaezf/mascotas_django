from django.shortcuts import render, redirect, HttpResponse
from .forms import MascotaForm
from .models import Mascota

# Create your views here.
def bienvenida(request):
    return render(request, 'main/bienvenida.html')


def mascotas(request):

    mascotas = ["Simba", "Dalila", "Negrita", "Chica", 'Fido']

    return render(request, 'mascotas/mascotas.html', {'mascotas': mascotas} )


def detalle_mascota(request, nombre):
    """
    Vista para mostrar los detalles de una mascota
    """
    detalles = {
                "Simba" : "Es una perrita marron",
                "Dalila" : "Es muy juguetona", 
                "Negrita" : "no hace caso, es muy loca",
                "Chica" : "Es una gatita dormilona",
                "Fido" : "Es muy curioso"
                }
    
    descripcion = detalles.get(nombre, "Mascota no encontrada.")

    return render(request, 'mascotas/detalle_mascota.html', {'nombre': nombre, 'descripcion': descripcion} )


def saludo(request, nombre):
    return HttpResponse(f"¡Hola, {nombre}")


def agregar_mascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'main/agregar_mascota.html', {'form': form})


def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    
    return render(request, 'main/lista_mascotas.html', {'mascotas' : mascotas})




