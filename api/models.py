from django.db import models


# Create your models here.
class Usuario(models.Model):
        rut = models.BigIntegerField(primary_key=True)
        clave = models.CharField(max_length=50)
        rol = models.CharField(max_length=50)


        def __int__(self):
            return self.rut 

class Bandejatrabajo(models.Model):
        idot = models.BigIntegerField(primary_key=True)
        idreserva = models.BigIntegerField()
        rutempleado = models.BigIntegerField()
        descripcionot = models.CharField(max_length=50)
        totalot = models.BigIntegerField()
        fechaot = models.CharField(max_length=50)
        estadoot = models.BigIntegerField()
        categoriaot = models.CharField(max_length=50)

        def __int__(self):
            return self.idot
class Reserva(models.Model):
        idreserva = models.BigIntegerField(primary_key=True)
        rutcliente = models.BigIntegerField()
        idservicio = models.BigIntegerField()
        fechareserva = models.CharField(max_length=50)
        horareserva = models.CharField(max_length=50)
        canal = models.CharField(max_length=50)
        patente = models.CharField(max_length=50)
        idvehiculo = models.BigIntegerField()
        ot_idot = models.BigIntegerField()
        ot_idreserva = models.BigIntegerField()

        def __int__(self):
            return self.idreserva  
        
class User(models.Model):
        
        rut = models.BigIntegerField(primary_key=True)
        nombre = models.CharField(max_length=100)
        telefono= models.BigIntegerField()
        email=models.CharField(max_length=100)
        password=models.CharField(max_length=50)
        rol = models.CharField(max_length=50)


        def __int__(self):
            return self.rut 

class Bandeja(models.Model):
        ot = models.BigIntegerField(primary_key=True)
        cliente = models.CharField(max_length=50)
        ingreso = models.CharField(max_length=50)
        equipo = models.CharField(max_length=50)
        termino = models.CharField(max_length=50)
        tarea = models.CharField(max_length=50)
        rutempleado = models.BigIntegerField()
        
        def __int__(self):
            return self.ot