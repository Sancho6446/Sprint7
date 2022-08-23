from pyexpat import model
from django.db import models

# Create your models here.
class Cuenta (models.Model):
    account_id = models.IntegerField()
    customer_id=models.IntegerField()
    balance=models.IntegerField()
    iban=models.TextField()

class Movimientos (models.Model):
    identificacion= models.IntegerField()
    nro_cuenta = models.IntegerField()
    monto=models.IntegerField()
    tipo_operacion=models.IntegerField()
    hora=models.DateTimeField()