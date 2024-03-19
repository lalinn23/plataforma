from django.urls import path
from .views import ActividadListCreate, ActividadDetail

urlpatterns = [
    path('actividad/', ActividadListCreate.as_view(), name='actividad-list-create'),
    path('actividad/<int:pk>/', ActividadDetail.as_view(), name='proyecto-detail'),
]