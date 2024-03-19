from django.db import models
from django.db.models import SET_NULL
from clientesApp.models import Clientes


class Proyecto(models.Model):
    nombreP = models.CharField(max_length=255)
    cliente = models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombreP

# NOTA
# Al querer eliminar no se ara en cascada por ende se aplica on_delete=SET_NULL null=True
