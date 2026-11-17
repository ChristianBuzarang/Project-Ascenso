from django.db import models
from django.contrib.auth.models import User


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Interface
    dark_mode = models.BooleanField(default=True)
    crt_scanlines = models.BooleanField(default=True)
    
    # AI & Audio Interventions
    ai_voice_interventions = models.BooleanField(default=True)
    voice_speed = models.CharField(max_length=20, default="Normal")
    
    # Biometric Detection & Safety
    biometric_sensitivity = models.CharField(max_length=20, default="Standard")
    auto_abort_timeout = models.IntegerField(default=10)
    
    # Telemetry & Notifications
    email_notifications = models.BooleanField(default=True)
    telemetry_sharing = models.BooleanField(default=False)

    class Meta:
        db_table = "user_settings"
        verbose_name_plural = "User Settings"

    def __str__(self):
        return f"Settings for {self.user.username}"
