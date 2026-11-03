from rest_framework import viewsets
from .models import Categoria, Producto, Pedido, DetallePedido
from .serializers import CategoriaSerializer, ProductoSerializer, PedidoSerializer, DetallePedidoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objets.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objets.all()
    serializer_class = ProductoSerializer
    
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objets.all()
    serializer_class = PedidoSerializer
    
class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objets.all()
    serializer_class = DetallePedidoSerializer
    