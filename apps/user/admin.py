# Django
from django.contrib import admin

# Project
from apps.user.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'is_active']
    list_display_links = ['phone_number']
    list_filter = ['is_active']
    search_fields = ['phone_number']
    ordering = ['-id']
