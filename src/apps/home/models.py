from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Datos_Adicionales(models.Model):
    nombre = models.CharField(
        unique=False,
        null=True,
        default="",
        max_length=32,
    )
    apellido = models.CharField(
        unique=False,
        null=True,
        default="",
        max_length=32,
    )
    dni = models.CharField(
        unique=True,
        null=False,
        default="",
        max_length=32,
    )
    edad = models.IntegerField(
        unique=False,
        null=False,
        default=-1,
    )

    class Meta:
        abstract = True


class User(AbstractUser, Datos_Adicionales):
    username: models.CharField(
        unique=True,
        null=False,
        verbose_name= "Nombre de Usuario",
        editable= False,
        max_length=32,
    )
    password: models.CharField(
        unique=True,
        null=False,
        max_length=32,
    )
    
    class Meta:
        db_table = "usuario"
        verbose_name = 'Usuario'
        verbose_name_plural = ' Usuarios'
        ordering = ['id']
