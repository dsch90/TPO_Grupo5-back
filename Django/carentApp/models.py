from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    correo_usuario = models.CharField(max_length=100)
    contacto_usuario =models.CharField(max_length=100)
    direccion_usuarios = models.CharField(max_length=100)
    password_usuario =models.CharField(max_length=100)
    
class Reserva(models.Model):
    horario_salida_reserva = models.DateTimeField(auto_now_add=True)
    horario_regreso_reserva = models.CharField(max_length=100)
    usuario_reserva = models.IntegerField()
    estado_reserva = models.IntegerField()
    vehiculo_reserva = models.IntegerField()

class Automovil(models.Model):
    nombre_automovil = models.CharField(max_length=100)
    descripcion_automovil = models.CharField(max_length=100)
    precio_automovil = models.IntegerField()
    marca_automovil = models.CharField(max_length=100)
    categoria_automovil = models.IntegerField()
    estado_automovil = models.IntegerField()
    foto_automovil = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_automovil

class Estado(models.Model):
    nombre = models.CharField(max_length=100)


class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

