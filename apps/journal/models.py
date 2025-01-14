from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Feliz'),
        ('grateful', 'Agradecido'),
        ('calm', 'Tranquilo'),
        ('motivated', 'Motivado'),
        ('reflective', 'Reflexivo')
    ]
    
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Contenido')
    mood = models.CharField('Estado de ánimo', max_length=10, choices=MOOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meta:
        ordering = ['-created_at']
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        
def __str__(self):
    return f'Entrada de {self.user.username} - {self.created_at.strftime("%d/%m/%Y")}'