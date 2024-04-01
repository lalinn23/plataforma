from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsAdminOrSuperUser(BasePermission):
    """
    Custom permission to only allow admins or superusers to access.
    """

    def has_permission(self, request, view):
        # Solo permitir acceso si el usuario es administrador o superusuario
        return request.user and (request.user.is_staff or request.user.is_superuser)

