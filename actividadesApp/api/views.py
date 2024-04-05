from rest_framework import generics
from actividadesApp.models import Actividad
from actividadesApp.api.serializer import ActividadSerializer
from actividadesApp.api.permission import IsNotAdmin

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter


class ActividadListCreate(generics.ListCreateAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer
    filter_backends = [OrderingFilter]  # Agregar el filtro de ordenación
    ordering_fields = ['created_at']



class ActividadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer
    # permission_classes = [IsNotAdmin]  # Asigna el permiso personalizado
