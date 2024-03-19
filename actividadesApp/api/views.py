from rest_framework import generics
from actividadesApp.models import Actividad
from actividadesApp.api.serializer import ActividadSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter


class ActividadListCreate(generics.ListCreateAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer


class ActividadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer