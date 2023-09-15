from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    class Meta:
        db_table = 'usuarios'