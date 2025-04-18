from django.contrib import admin
from .models import Profile, Achievement

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_streak', 'best_streak', 'last_entry_date', 'created_at', 'updated_at')
    list_filter = ('current_streak', 'last_entry_date')
    search_fields = ('user__username',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement_type', 'earned_date')
    list_filter = ('achievement_type', 'earned_date')
    search_fields = ('user__username',)
    readonly_fields = ('earned_date',)