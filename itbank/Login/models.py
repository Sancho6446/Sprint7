from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class nuevoUsuario(models.Model):
    nombreUsuario = models.CharField(max_length=10)
    contraseña = models.CharField(max_length=10)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
