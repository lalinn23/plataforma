from rest_framework.routers import DefaultRouter
from proyectosApp.api.views import ProyectoApiViewSet


router_proyecto = DefaultRouter()

router_proyecto.register(prefix='proyecto', basename='proyecto', viewset=ProyectoApiViewSet)