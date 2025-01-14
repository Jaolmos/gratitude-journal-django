from django.urls import path
from .views import DashboardView, EntryCreateView

app_name = 'journal'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('entry/new/', EntryCreateView.as_view(), name='entry_create'),
]