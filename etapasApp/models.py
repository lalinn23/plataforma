from django.db import models

# Create your models here.


class Etapa(models.Model):
    nombreE = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombreE