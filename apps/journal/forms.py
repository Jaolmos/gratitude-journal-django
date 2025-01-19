from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['content', 'mood']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': '¿Por qué estás agradecido hoy?',
                'rows': '6',
                'class': 'form-control'
            }),
            'mood': forms.Select(attrs={'class': 'form-select'})
        }