from datetime import date, timedelta
from django.utils import timezone
from .models import Achievement

def check_achievements(profile):
    """
    Verifica y otorga logros basados en la racha actual del usuario.
    """
    streak_achievements = [
        (7, 'WEEK'),      # Semana Constante
        (30, 'MONTH'),    # Mes Dedicado
        (90, 'QUARTER'),  # Trimestre de Gratitud
        (180, 'HALF_YEAR'), # Medio Año de Reflexión
        (365, 'YEAR')     # Maestro de la Gratitud
    ]
    
    for days, achievement_type in streak_achievements:
        if profile.current_streak >= days:
            # Intentar crear el logro si no existe
            Achievement.objects.get_or_create(
                user=profile.user,
                achievement_type=achievement_type
            )

def update_user_streak(profile):
    """
    Actualiza la racha del usuario basándose en su última entrada.
    """
    today = timezone.now().date()
    
    # Si no hay última entrada, es la primera vez
    if not profile.last_entry_date:
        profile.current_streak = 1
        profile.best_streak = max(profile.best_streak, 1)
        profile.last_entry_date = today
        profile.save()
        check_achievements(profile)
        return
    
    # Si la última entrada fue ayer, incrementamos la racha
    if profile.last_entry_date == today - timedelta(days=1):
        profile.current_streak += 1
        profile.best_streak = max(profile.best_streak, profile.current_streak)
    # Si la última entrada fue hoy, mantenemos la racha
    elif profile.last_entry_date == today:
        pass
    # Si hay un salto de días, reiniciamos la racha
    else:
        profile.current_streak = 1
    
    profile.last_entry_date = today
    profile.save()
    
    # Verificar logros después de actualizar la racha
    check_achievements(profile) 