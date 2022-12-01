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

class Cliente(models.Model):
        rutcliente = models.BigIntegerField(primary_key=True)
        dvcliente = models.CharField(max_length=1)
        nombre = models.CharField(max_length=50)
        appaterno = models.CharField(max_length=50)
        apmaterno = models.CharField(max_length=50)

        def __int__(self):
            return self.rutcliente


class Empleado(models.Model):
        rutempleado = models.BigIntegerField(primary_key=True)
        dvempleado = models.CharField(max_length=1)
        nombre = models.CharField(max_length=50)
        appaterno = models.CharField(max_length=50)
        apmaterno = models.CharField(max_length=50)
        rol = models.CharField(max_length=50)

        def __int__(self):
            return self.rutempleado


class Facturacion(models.Model):
        nrodocumento = models.BigIntegerField(primary_key=True)
        tipodocumento = models.CharField(max_length=50)
        idot = models.BigIntegerField()
        ot_idot = models.BigIntegerField()
        ot_idreserva = models.BigIntegerField()

        def __int__(self):
            return self.nrodocumento 

class Ot(models.Model):
        idot = models.BigIntegerField(primary_key=True)
        idreserva = models.BigIntegerField()
        rutempleado = models.BigIntegerField()
        descripcionot = models.CharField(max_length=50)
        totalot = models.BigIntegerField()
        fechaot = models.DateField(blank=True, null=True)
        reserva_idreserva = models.CharField(max_length=50)
        facturacion_nrodocumento = models.BigIntegerField()
        facturacion_idot = models.BigIntegerField()

        def __int__(self):
            return self.idot 

class Productos(models.Model):
        idproducto = models.BigIntegerField(primary_key=True)
        nombreproducto = models.CharField(max_length=50)
        cantidad = models.BigIntegerField()
        tipoproducto = models.CharField(max_length=50)
        marcaproducto = models.CharField(max_length=50)
        idvehiculo = models.BigIntegerField()
        valorproducto = models.BigIntegerField()
        rutproveedor = models.BigIntegerField()

        def __int__(self):
            return self.idproducto  


class Proveedor(models.Model):
        rutproveedor = models.BigIntegerField(primary_key=True)
        dvproveedor = models.CharField(max_length=1)
        nombreproveedor = models.CharField(max_length=50)
        direccionproveedor = models.CharField(max_length=50)
        telefonocontacto = models.CharField(max_length=50)
        email = models.CharField(max_length=50)

        def __int__(self):
            return self.rutproveedor 


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


class Servicio(models.Model):
        idservicio = models.BigIntegerField(primary_key=True)
        tiposervicio = models.CharField(max_length=50)
        descservicio = models.CharField(max_length=50)
        valorservicio = models.BigIntegerField()

        def __int__(self):
            return self.idservicio 



class Vehiculos(models.Model):
        idvehiculo = models.BigIntegerField(primary_key=True)
        marca = models.CharField(max_length=50)
        modelo = models.CharField(max_length=50)
        anio = models.BigIntegerField()
        tipovehiculo = models.CharField(max_length=50)
        cilindrada = models.BigIntegerField()
        vin = models.CharField(max_length=50)
        reserva_idreserva = models.BigIntegerField()

        def __int__(self):
            return self.idvehiculo 