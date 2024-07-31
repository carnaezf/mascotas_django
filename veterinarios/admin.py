from django.contrib import admin
from .models import Veterinario

# Register your models here.
# Registrar el modelo Veterinario para que sea gestionable desde el admin
admin.site.register(Veterinario)
