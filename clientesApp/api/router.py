from rest_framework.routers import DefaultRouter
from clientesApp.api.views import ClientesApiViewSet

router_clientes = DefaultRouter()

router_clientes.register(prefix='clientes', basename='clientes', viewset=ClientesApiViewSet)

