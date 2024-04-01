from django.contrib.auth import authenticate, logout, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.api.serializers import UserRegisterSerializer,  UserLoginSerializer, UserSerializer
from users.models import User


User = get_user_model()

class UsersListView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'message': 'El usuario no existe'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'message': 'Usuario eliminado exitosamente'}, status=status.HTTP_204_NO_CONTENT)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        try:
            # Validar campos
            if 'email' not in request.data:
                return Response({'message': 'El correo es requerido.'}, status=status.HTTP_401_UNAUTHORIZED)

            if 'password' not in request.data:
                return Response({'message': 'La contraseña es requerida.'}, status=status.HTTP_401_UNAUTHORIZED)

            email = request.data.get('email')
            password = request.data.get('password', None)

            # Validar si el usuario existe
            user_exist = User.objects.filter(email=email).first()
            if not user_exist:
                return Response({'message': 'El correo proporcionado no existe.'}, status=status.HTTP_401_UNAUTHORIZED)

            # Autenticar el usuario
            user = authenticate(request, username=user_exist.username, password=password)
            if user is not None:
                if not user_exist.is_active:
                    return Response({'message': 'La cuenta está desactivada.'}, status=status.HTTP_401_UNAUTHORIZED)

                # Obtener el rol del usuario
                #role = 'admin' if user_exist.is_staff else 'normal'
                if user_exist.is_staff:

                    return Response({'message': 'Login successful', 'role': 'admin'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Login successful', 'role': 'normal'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(e)
            return Response({'msg': 'Error en el servicio', 'ex': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        try:
            logout(request)  # Cierra la sesión del usuario
        except Exception as e:
            return Response({'message': 'Error al cerrar sesión'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Sesión cerrada exitosamente'}, status=status.HTTP_200_OK)
