from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True) #hace que email sea primero que user

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


