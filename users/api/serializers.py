from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'puesto']


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()  # Agregar el campo username

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'puesto', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data.pop('username')  # Extraer el campo username
        user = User.objects.create_user(username=username, **validated_data)  # Pasar username como argumento
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


