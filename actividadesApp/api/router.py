from rest_framework.routers import DefaultRouter
from actividadesApp.api.views import ActividadApiViewSet


router_actividad = DefaultRouter()

router_actividad.register(prefix='actividad', basename='actividad', viewset=ActividadApiViewSet)