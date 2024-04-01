from rest_framework import generics
from proyectosApp.models import Proyecto
from proyectosApp.api.serializer import ProyectoSerializer
from proyectosApp.api.permission import IsAdminOnly

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProyectoListCreate(generics.ListCreateAPIView):
    # permission_classes = [IsAdminOnly]
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer


class ProyectoDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminOnly]
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer