from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(
        'Biografía',
        max_length=500, 
        blank=True
    )
    created_at = models.DateTimeField(
        'Fecha de creación',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Fecha de actualización',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return f'Perfil de {self.user.username}'