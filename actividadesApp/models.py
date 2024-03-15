from django.db import models
from django.db.models import SET_NULL
from users.models import User
from proyectosApp.models import Proyecto
from fasesApp.models import Fases
from etapasApp.models import Etapa


class Actividad(models.Model):
    lider = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    user = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=SET_NULL, null=True)
    actividad = models.CharField(max_length=255)
    fase = models.ForeignKey(Fases, on_delete=SET_NULL, null=True)
    etapa = models.ForeignKey(Etapa, on_delete=SET_NULL, null=True)
    descripcion = models.TextField()
    hora = models.DecimalField(max_digits=10, decimal_places=2)



