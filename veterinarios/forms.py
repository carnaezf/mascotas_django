from django import forms
from .models import Veterinario

# Formulario basado en el modelo Veterinario
class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'especialidad', 'telefono', 'email']
