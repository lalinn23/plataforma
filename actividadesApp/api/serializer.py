from rest_framework import serializers
from actividadesApp.models import Actividad


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['id','lider', 'user', 'created_at', 'proyecto', 'actividad', 'fase', 'etapa', 'descripcion', 'hora']