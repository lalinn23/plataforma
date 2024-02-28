from rest_framework.viewsets import ModelViewSet
from etapasApp.models import Etapa
from etapasApp.api.serializer import EtapaSerializer


class EtapaApiViewSet(ModelViewSet):
    serializer_class = EtapaSerializer
    queryset = Etapa.objects.all()
