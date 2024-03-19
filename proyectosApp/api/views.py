from rest_framework import generics
from proyectosApp.models import Proyecto
from proyectosApp.api.serializer import ProyectoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProyectoListCreate(generics.ListCreateAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer


class ProyectoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer