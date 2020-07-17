from django import forms
from django.forms import ModelForm
from autos.modelo.models import Automovil, Busqueda


# Formulario para agregar un vehiculo.
class nuevoAutoForm(ModelForm):
    class Meta:
        model = Automovil
        fields = ('marca', 'modelo', 'puertas', 'anio', 'descripcion')


# formulario de busquedas de automoviles.
class filtrarAutosForm(ModelForm):
    class Meta:
        model = Busqueda
        fields = ['marca']