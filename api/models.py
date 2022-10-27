from django.db import models


# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
        nombre =models.CharField(max_length=50)
        apellido =models.CharField(max_length=50)
        rut =models.CharField(max_length=12)
        fnacimiento =models.DateField()
        email = models.EmailField()
        password =models.CharField(max_length=30)
        direccion =models.CharField(max_length=100)
        telefono = models.CharField(max_length=9)
        direccionCom =models.CharField(max_length=100)
        telefonoCom =models.CharField(max_length=9)
        rol = models.ForeignKey(Rol, on_delete=models.PROTECT)


        def __str__(self):
            return self.nombre