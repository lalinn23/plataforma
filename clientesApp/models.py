from django.db import models

# Create your models here.


class Clientes(models.Model):
    nombreC = models.CharField(max_length=250, unique=True)
    published = models.BooleanField(default=False)

    # cuando se despliege mostrara el nombre
    def __str__(self):
        return self.nombreC
