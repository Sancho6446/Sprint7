from django.db import models

# Create your models here.
class Cliente (models.Model):
    customer_id = models.IntegerField()
    customer_name=models.TextField()
    customer_surname=models.TextField()
    customer_DNI=models.IntegerField()
    dob=models.TextField()
    branch_id=models.TextField()

class Empleados (models.Model):
    employedd_id = models.IntegerField()
    employedd_name=models.TextField()
    employedd_surname=models.TextField()
    employedd_DNI=models.IntegerField()
    branch_id=models.TextField()
