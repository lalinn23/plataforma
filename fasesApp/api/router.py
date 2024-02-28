from rest_framework.routers import DefaultRouter
from fasesApp.api.views import FasesApiViewSet


router_fases = DefaultRouter()

router_fases.register(prefix='fases', basename='fases', viewset=FasesApiViewSet)
