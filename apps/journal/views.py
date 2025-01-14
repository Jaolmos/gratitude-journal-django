from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Entry
from .forms import EntryForm

class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'journal/entry_form.html'
    success_url = reverse_lazy('journal:dashboard')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)