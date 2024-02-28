from rest_framework import serializers
from proyectosApp.models import Proyecto
from clientesApp.api.serializer import ClientesSerializers


class ProyectoSerializer(serializers.ModelSerializer):
    cliente = ClientesSerializers() # muestra la info del FK

    class Meta:
        model = Proyecto
        fields = ['id', 'nombreP', 'created_at', 'published', 'cliente']