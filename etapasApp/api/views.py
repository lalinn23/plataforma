from rest_framework.viewsets import ModelViewSet
from etapasApp.models import Etapa
from etapasApp.api.serializer import EtapaSerializer
from etapasApp.api.permission import IsAdminOnly



class EtapaApiViewSet(ModelViewSet):
    # permission_classes = [IsAdminOnly]
    serializer_class = EtapaSerializer
    queryset = Etapa.objects.all()
