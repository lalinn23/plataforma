from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True) #hace que email sea primero que user
    puesto = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username



