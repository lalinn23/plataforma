from rest_framework import serializers
from proyectosApp.models import Proyecto
from clientesApp.models import Clientes
from clientesApp.api.serializer import ClientesSerializers


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ['id', 'nombreC']


class ProyectoSerializer(serializers.ModelSerializer):
    cliente_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Proyecto
        fields = ['id', 'nombreP', 'cliente','cliente_id']
        depth = 1