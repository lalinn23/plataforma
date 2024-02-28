from django.db import models
from django.db.models import SET_NULL
from clientesApp.models import Clientes


class Proyecto(models.Model):
    nombreP = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    cliente = models.ForeignKey(Clientes, on_delete=SET_NULL, null=True)


    def __str__(self):
        return self.nombreP

# NOTA
# Al querer eliminar no se ara en cascada por ende se aplica on_delete=SET_NULL null=True

