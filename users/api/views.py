from rest_framework.views import APIView
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    # permission_classes = [IsAuthenticated] #para los permisos
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, pk: int):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
