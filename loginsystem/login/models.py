from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'usuarios'