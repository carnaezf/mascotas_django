from django.shortcuts import render, HttpResponse

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
