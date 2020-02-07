from django.db import models
from model_utils import Choices

class Sala(models.Model):
    nombre = models.CharField(max_length=50)
    aporte_mensual_sugerido = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre

class Niñe(models.Model):    
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    sala = models.ForeignKey('Sala')
    responsables = models.ManyToManyField('Responsable', through='RelacionResponsable')

    def __str__(self):
        return f"{self.nombre} ({self.sala})"


class RelacionResponsable(models.Model):
    RELACIONES = Choices('mamá', 'papá', 'otro')
    relacion = models.CharField(max_length=50, choices=RELACIONES)
    niñe = models.ForeignKey('Niñe')
    responsable = models.ForeignKey('Responsable')

# Create your models here.
class Responsable(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField('Teléfono', max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"