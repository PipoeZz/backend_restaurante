from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    completado = models.BooleanField(default=False)

    def actualizar_total(self): # suma los subtotales de los platos hacia la boleta
        self.total = sum(detalle.subtotal for detalle in self.detalles.all())
        self.save()

    def __str__(self):
        return f"Pedido {self.id} - Total: ${self.total}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    subtotal = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.subtotal = self.producto.precio * self.cantidad # intercepta el guardado y calcula el subtotal (precio real x cantidad)
        super().save(*args, **kwargs) # guarda el detalle en la base de datos
        from .models import Pedido
        pedido_fresco = Pedido.objects.get(id=self.pedido.id) # obtiene la boleta actualizada desde la base de datos
        pedido_fresco.actualizar_total() # le ordena a la boleta que recalcule su total sumando todo

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} en Pedido {self.pedido.id}"