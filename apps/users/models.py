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
    # Campos para el sistema de rachas
    current_streak = models.IntegerField(
        'Racha actual',
        default=0,
        help_text='Días consecutivos escribiendo en el diario'
    )
    best_streak = models.IntegerField(
        'Mejor racha',
        default=0,
        help_text='Mayor número de días consecutivos alcanzado'
    )
    last_entry_date = models.DateField(
        'Última entrada',
        null=True,
        blank=True,
        help_text='Fecha de la última entrada en el diario'
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

class Achievement(models.Model):
    ACHIEVEMENT_TYPES = [
        ('WEEK', 'Semana Constante'),
        ('MONTH', 'Mes Dedicado'),
        ('QUARTER', 'Trimestre de Gratitud'),
        ('HALF_YEAR', 'Medio Año de Reflexión'),
        ('YEAR', 'Maestro de la Gratitud')
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='achievements',
        verbose_name='Usuario'
    )
    achievement_type = models.CharField(
        'Tipo de Logro',
        max_length=20,
        choices=ACHIEVEMENT_TYPES
    )
    earned_date = models.DateTimeField(
        'Fecha de obtención',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Logro'
        verbose_name_plural = 'Logros'
        # Evitar duplicados del mismo logro para el mismo usuario
        unique_together = ['user', 'achievement_type']

    def __str__(self):
        return f'{self.get_achievement_type_display()} - {self.user.username}'