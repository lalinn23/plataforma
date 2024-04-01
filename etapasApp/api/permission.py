from rest_framework.permissions import BasePermission
from rest_framework import permissions

# si el usuario no es admin solo podra consultar
# si es admin realizar crud


class IsAdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


