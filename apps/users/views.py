from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        # Enviar correo de bienvenida
        self.send_welcome_email(user)
        login(self.request, user)
        return redirect('home')
    
    def send_welcome_email(self, user):
        subject = 'Bienvenido a Diario de Gratitud'
        html_message = render_to_string('emails/welcome_email.html', {
            'user': user,
        })
        plain_message = f"¡Hola {user.username}! Gracias por registrarte en Diario de Gratitud."
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = user.email
        
        send_mail(
            subject,
            plain_message,
            from_email,
            [to_email],
            html_message=html_message,
            fail_silently=False,
        )
class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('journal:dashboard')
    
    
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'users/profile_form.html'
    fields = ['bio']
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    

