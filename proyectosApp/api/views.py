from rest_framework.viewsets import ModelViewSet
from proyectosApp.models import Proyecto
from proyectosApp.api.serializer import ProyectoSerializer
from proyectosApp.api.permission import IsAdminOrReadOnly


class ProyectoApiViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly] #permisos
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
