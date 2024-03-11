from rest_framework import serializers
from fasesApp.models import Fases


class FaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fases
        fields = ['id','nombreF']