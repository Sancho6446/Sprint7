from http import client
from django.db import models

# Create your models here.
class Tarjeta(models.Model):
    numero= models.IntegerField()
    CVV = models.IntegerField()
    Fecha_otor=models.DateTimeField()
    Fecha_exp=models.DateTimeField()
    tipo_tarjeta=models.TextField()
    marca=models.TextField()
    client_cuenta=models.IntegerField()