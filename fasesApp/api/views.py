from rest_framework.viewsets import ModelViewSet
from fasesApp.models import Fases
from fasesApp.api.serializer import FaseSerializer
from fasesApp.api.permission import IsAdminOnly



class FasesApiViewSet(ModelViewSet):
    # permission_classes = [IsAdminOnly]
    serializer_class = FaseSerializer
    queryset = Fases.objects.all()