from django.db import models


class tipoProducto (models.Model):
    tipoProducto = models.CharField(max_length=100)
    descripcionTipoProducto = models.CharField(max_length=100)


class Producto (models. Model):
    nombreProducto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    descripcionProducto = models.CharField(max_length=100)
    idTipoProducto = models.ForeignKey(tipoProducto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombreProducto


class Cliente (models.Model):
    nombreCliente = models.CharField(max_length=50)
    telefonoCliente = models.IntegerField()
    correo = models.EmailField()


class Proyecto (models.Model):
    nombreProyecto = models.CharField(max_length=50)
    descripcionProyecto = models.CharField(max_length=100)
    estadoProyecto = models.CharField(max_length=100)
    id_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)


class Bodega (models.Model):
    nombreBodega = models.CharField(max_length=50)
    direccionBodega = models.CharField(max_length=100)


class productoBodega (models.Model):
    stock = models.IntegerField()
    id_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_Bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
