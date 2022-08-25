from django.db import models
from django.contrib.auth.models import User
from cuentas.models import Cliente

# Create your models here.

class Usuario(User):
    customer = models.OneToOneField(
        Cliente, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
