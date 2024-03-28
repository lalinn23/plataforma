from django.contrib.auth import authenticate, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.api.serializers import UserRegisterSerializer,  UserLoginSerializer, UserSerializer
from users.models import User


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
            #validar campos
            if 'email' not in request.data:
                return Response({'message': 'El correo es requerido.'}, status=status.HTTP_401_UNAUTHORIZED)

            if 'password' not in request.data:
                return Response({'message': 'La contraseña es requerida.'}, status=status.HTTP_401_UNAUTHORIZED)

            email = request.data.get('email')
            password = request.data.get('password', None)

            #Validar si el usuarioe existe
            user_exist = User.objects.filter(email=email)
            if len(user_exist) == 0 or None:
                return Response({'message': 'El correo proporcionado no existe.'}, status=status.HTTP_401_UNAUTHORIZED)

            #autenticar el usuario
            user = authenticate(request, username=user_exist.get().username, password=password)
            if user is not None:
                if not user_exist.get().is_active:
                    return Response({'message': 'La contraseña es requerida.'}, status=status.HTTP_401_UNAUTHORIZED)

                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'credenciales invalidas'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(e)
            return Response({'msg': 'Error en el servicio', 'ex': e.__str__()}, status=status.HTTP_400_BAD_REQUEST)



class LogoutView(APIView):
    def post(self, request):
        try:
            logout(request)  # Cierra la sesión del usuario
        except Exception as e:
            return Response({'message': 'Error al cerrar sesión'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Sesión cerrada exitosamente'}, status=status.HTTP_200_OK)
