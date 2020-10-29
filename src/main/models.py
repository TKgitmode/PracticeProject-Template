from django.db import models

# Create your models here.
# needed to work with bd
# Entities

class Repuesto(models.Model):
    stock=models.IntegerField()
    nombre=models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)
    fecha_manual=models.TextField()

