"""
URL configuration for plataforma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from clientesApp.api.router import router_clientes
from proyectosApp.api.router import router_proyecto
from fasesApp.api.router import router_fases
from etapasApp.api.router import router_etapa
from actividadesApp.api.router import router_actividad


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.api.router')),
    path('api/cliente/', include(router_clientes.urls)),
    path('api/proyecto/', include(router_proyecto.urls)),
    path('api/fase/', include(router_fases.urls)),
    path('api/etapa/', include(router_etapa.urls)),
    path('api/actividad/', include(router_actividad.urls))

]
