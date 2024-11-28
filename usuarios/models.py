from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_perfil', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    ubicacion = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.user.username} Perfil'
