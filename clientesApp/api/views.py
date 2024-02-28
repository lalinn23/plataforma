from rest_framework.viewsets import ModelViewSet
from clientesApp.models import Clientes
from clientesApp.api.serializer import ClientesSerializers
from clientesApp.api.permission import IsAdminOrReadOnly
# realiza el crud



class ClientesApiViewSet(ModelViewSet):
   # permission_classes = [IsAdminOrReadOnly] # permiso
    serializer_class = ClientesSerializers
    #queryset = Clientes.objects.all()
    queryset = Clientes.objects.filter(published=True) # filtrado por true
