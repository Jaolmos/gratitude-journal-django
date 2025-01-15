from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    date_hierarchy = 'date_joined'

    # Campos en el formulario de edición
    fieldsets = (
        ('Información Personal', {'fields': ('username', 'password', 'email', 'first_name', 'last_name')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )