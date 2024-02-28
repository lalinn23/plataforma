from rest_framework import serializers
from clientesApp.models import Clientes


class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ['id', 'nombreC', 'published']