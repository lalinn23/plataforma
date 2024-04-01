from rest_framework.viewsets import ModelViewSet
from clientesApp.models import Clientes
from clientesApp.api.serializer import ClientesSerializers
from clientesApp.api.permission import IsAdminOrSuperUser

# realiza el crud


class ClientesApiViewSet(ModelViewSet):
    serializer_class = ClientesSerializers
    queryset = Clientes.objects.all()
    # permission_classes = [IsAdminOrSuperUser]