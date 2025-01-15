from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'mood', 'created_at')
    list_filter = ('mood', 'created_at')
    search_fields = ('content',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')