from rest_framework import serializers
from etapasApp.models import Etapa


class EtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields = ['id', 'nombreE']
