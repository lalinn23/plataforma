from rest_framework.permissions import BasePermission

class IsNotAdmin(BasePermission):
    """
    Permiso personalizado que permite el acceso a los usuarios que no son administradores.
    """
    def has_permission(self, request, view):
        return request.user and not request.user.is_staff