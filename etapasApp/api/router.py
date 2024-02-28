from rest_framework.routers import DefaultRouter
from etapasApp.api.views import EtapaApiViewSet

router_etapa = DefaultRouter()

router_etapa.register(prefix='etapas', basename='etapas', viewset=EtapaApiViewSet)