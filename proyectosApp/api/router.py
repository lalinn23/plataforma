from django.urls import path
from . import views
from .views import ProyectoListCreate, ProyectoDetail

urlpatterns = [
    path('proyectos/', ProyectoListCreate.as_view(), name='proyecto-list-create'),
    path('proyectos/<int:pk>/', ProyectoDetail.as_view(), name='proyecto-detail'),

]