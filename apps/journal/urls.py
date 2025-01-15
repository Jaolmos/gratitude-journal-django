from django.urls import path
from .views import DashboardView, EntryCreateView, EntryListView, EntryUpdateView, EntryDeleteView

app_name = 'journal'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('entry/new/', EntryCreateView.as_view(), name='entry_create'),
    path('entries/', EntryListView.as_view(), name='entry_list'),
    path('entry/<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_update'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry_delete'),
    
]