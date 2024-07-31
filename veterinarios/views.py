from django.shortcuts import render, redirect
from .models import Veterinario
from .forms import VeterinarioForm

# Vista para listar los veterinarios
def lista_veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'veterinarios/lista_veterinarios.html', {'veterinarios': veterinarios})

# Vista para agregar un nuevo veterinario
def agregar_veterinario(request):
    if request.method == "POST":
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_veterinarios')
    else:
        form = VeterinarioForm()
    return render(request, 'veterinarios/agregar_veterinario.html', {'form': form})
