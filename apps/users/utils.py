from datetime import date, timedelta
from django.utils import timezone

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