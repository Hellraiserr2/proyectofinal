from django.db import models


class Planta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='plantas/')
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.TextField()

class DetallePedido(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    planta = models.ForeignKey('Planta', on_delete=models.CASCADE)
    cantidad = models.IntegerField()