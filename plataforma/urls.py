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
from django.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users.api.views import RegisterView, LoginView, UsersListView, UserDetailView, LogoutView
from clientesApp.api.router import router_clientes
from proyectosApp.api.router import urlpatterns as proyectos_urls
from fasesApp.api.router import router_fases
from etapasApp.api.router import router_etapa
from actividadesApp.api.router import urlpatterns as actividad_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api_authorization/', include('rest_framework.urls')),
    path('users/', UsersListView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('api/cliente/', include(router_clientes.urls)),
    path('api/',include(proyectos_urls)),  # Importa las URLs de proyectosApp
    path('api/fase/', include(router_fases.urls)),
    path('api/etapa/', include(router_etapa.urls)),
    path('api/', include(actividad_urls))

]
