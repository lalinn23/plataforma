from rest_framework.permissions import BasePermission

# si el usuario no es admin solo podra consultar
# si es admin realizar crud


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff


