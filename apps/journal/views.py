from django.db import models
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Entry
from .forms import EntryForm
from django.contrib import messages
from django.http import HttpResponse
from apps.users.utils import update_user_streak
from apps.users.models import Achievement

class HomeView(TemplateView):
    template_name= 'home.html'

class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'journal/entry_form.html'
    success_url = reverse_lazy('journal:dashboard')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        # Actualizar la racha del usuario
        update_user_streak(self.request.user.profile)
        return response
    
class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'journal/entry_list.html'
    context_object_name = 'entries'
    paginate_by = 10

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user).order_by('-created_at')
    
class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'journal/entry_form.html'
    success_url = reverse_lazy('journal:entry_list')
    
class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    template_name = 'journal/entry_confirm_delete.html'
    success_url = reverse_lazy('journal:entry_list')
    
    def post(self, request, *args, **kwargs):
        # Si es una petición HTMX, eliminamos directamente
        if request.headers.get('HX-Request'):
            self.object = self.get_object()
            self.object.delete()
            #  devolvemos una respuesta vacía
            return HttpResponse("")
           
        # Si no es HTMX, seguimos el flujo normal con confirmación
        return super().post(request, *args, **kwargs)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'journal/dashboard.html'

    def get_next_achievement_info(self, current_streak):
        """Obtiene información sobre el siguiente logro a alcanzar."""
        achievement_levels = [
            (7, 'Semana Constante'),
            (30, 'Mes Dedicado'),
            (90, 'Trimestre de Gratitud'),
            (180, 'Medio Año de Reflexión'),
            (365, 'Maestro de la Gratitud')
        ]
        
        for days, name in achievement_levels:
            if current_streak < days:
                return {
                    'name': name,
                    'days_required': days,
                    'days_remaining': days - current_streak,
                    'progress': (current_streak / days) * 100
                }
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_entries = Entry.objects.filter(user=self.request.user)
        
        # Últimas entradas (limitadas a 5)
        context['latest_entries'] = user_entries.order_by('-created_at')[:5]
        
        # Estadísticas básicas
        context['total_entries'] = user_entries.count()
        context['most_common_mood'] = (
            user_entries.values('mood')
            .annotate(count=models.Count('mood'))
            .order_by('-count')
            .first()
        )
        
        # Información de rachas
        profile = self.request.user.profile
        context['current_streak'] = profile.current_streak
        context['best_streak'] = profile.best_streak
        context['last_entry_date'] = profile.last_entry_date

        # Logros conseguidos
        context['achievements'] = Achievement.objects.filter(
            user=self.request.user
        ).order_by('earned_date')

        # Información del próximo logro
        next_achievement = self.get_next_achievement_info(profile.current_streak)
        if next_achievement:
            context['next_achievement'] = next_achievement

        return context
