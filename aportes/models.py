from django.db import models
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices


class Aporte(StatusModel, TimeStampedModel):
    STATUS = Choices('cobrado', 'rendido')
    niñe = models.ForeignKey('familias.Niñe')
    monto = models.DecimalField(max_digits=5, decimal_places=2)
    concepto= models.CharField(max_length=50, null=True, blank=True)
    cobrado_por = models.ForeignKey('auth.User')
    comentario = models.TextField()


    def __str__(self):
        return f'{self.niñe}: $ {self.monto}'
