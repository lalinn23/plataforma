from django.db import models

# Create your models here.


class Etapa(models.Model):
    nombreE = models.CharField(max_length=255)

    def __str__(self):
        return self.nombreE