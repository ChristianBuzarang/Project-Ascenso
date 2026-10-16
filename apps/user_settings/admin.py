from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import UserSettings


@admin.register(UserSettings)
class UserSettingsAdmin(ModelAdmin):
    list_display = ("user", "dark_mode", "email_notifications")
