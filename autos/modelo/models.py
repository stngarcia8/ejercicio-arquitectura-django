from django.db import models
from django.core.validators import MaxValueValidator


# modelo para el automovil.
class Automovil(models.Model):

    #Marcas aceptadas.
    marcas = (('', 'Seleccione una marca'), ('Suzuki', 'Suzuki'), ('Hiunday',
                                                                   'Hiunday'))

    # Atributos del modelo.
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50, choices=marcas, default='')
    modelo = models.CharField(max_length=25, verbose_name='Modelo')
    puertas = models.PositiveIntegerField(
        validators=[MaxValueValidator(6)], verbose_name='Cantidad de puertas')
    anio = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999)], verbose_name='Año')
    descripcion = models.TextField(max_length=100)

    # Metodo str de la clase
    def __str__(self):
        return self.modelo + " " + self.marca + " " + self.anio


# Modelo para realizar las busquedas por marca
class Busqueda(models.Model):
    #Marcas aceptadas.
    marcas = (('Todos', 'Todas las marcas'), ('Suzuki', 'Suzuki'), ('Hiunday',
                                                                    'Hiunday'))

    # Atributos de la clase.
    marca = models.CharField(max_length=50, choices=marcas, default='Todos')

    # Metodo str de la clase.
    def __str__(self):
        return self.marca