from django.db import models

class Usuario(models.Model):
    usuario=models.CharField(primary_key=True ,max_length=30)
    correo=models.EmailField(unique=True,max_length=100, blank=True, null=True)
    contraseña=models.CharField(max_length=30)
    def __str__(self):
        return str(self.usuario)


class Producto(models.Model):
    nombreProducto=models.CharField(primary_key=True ,max_length=30)
    precio=models.CharField(max_length=30)
    stock=models.CharField(max_length=30)

    def __str__(self):
        return str(self.nombreProducto)
    
    


