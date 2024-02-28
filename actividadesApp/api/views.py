from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from actividadesApp.models import Actividad
from actividadesApp.api.serializer import ActividadSerializer


class ActividadApiViewSet(ModelViewSet):
    serializer_class = ActividadSerializer
    queryset = Actividad.objects.all()
    filter_backends = [OrderingFilter]
    ordering = ['-created_at']