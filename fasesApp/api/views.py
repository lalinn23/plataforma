from rest_framework.viewsets import ModelViewSet
from fasesApp.models import Fases
from fasesApp.api.serializer import FaseSerializer


class FasesApiViewSet(ModelViewSet):
    serializer_class = FaseSerializer
    queryset = Fases.objects.all()