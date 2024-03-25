from rest_framework import serializers
from actividadesApp.models import Actividad


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['id','username']


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['id', 'nombreP']


class FaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['id','nombreF']


class EtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['id', 'nombreE']


class ActividadSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    proyecto_id = serializers.IntegerField(write_only=True)
    fase_id = serializers.IntegerField(write_only=True)
    etapa_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Actividad
        fields = ['id',
                  'lider',
                  'user','user_id',
                  'created_at',
                  'proyecto','proyecto_id',
                  'actividad',
                  'fase','fase_id',
                  'etapa','etapa_id',
                  'descripcion',
                  'hora']
        depth = 1