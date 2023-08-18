from django.db import models

# Create your models here.
class Formulario1(models.Model):
    moneda = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Formulario2(models.Model):
    instrumento = models.CharField(max_length=100)
    factor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.instrumento