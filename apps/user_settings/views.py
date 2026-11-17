from django.contrib.auth import views
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserSettings


@login_required(login_url="login:login")
def settings_view(request):
    settings_obj, created = UserSettings.objects.get_or_create(user=request.user)

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "reset":
            settings_obj.dark_mode = True
            settings_obj.crt_scanlines = True
            settings_obj.ai_voice_interventions = True
            settings_obj.voice_speed = "Normal"
            settings_obj.biometric_sensitivity = "Standard"
            settings_obj.auto_abort_timeout = 10
            settings_obj.email_notifications = True
            settings_obj.telemetry_sharing = False
            settings_obj.save()
            messages.success(request, "System Preferences Restored to Factory Defaults.")
            return redirect("user_settings:settings")

        # Update all preference fields
        settings_obj.dark_mode = request.POST.get("dark_mode") == "on"
        settings_obj.crt_scanlines = request.POST.get("crt_scanlines") == "on"
        settings_obj.ai_voice_interventions = (
            request.POST.get("ai_voice_interventions") == "on"
        )
        settings_obj.voice_speed = request.POST.get("voice_speed", "Normal")
        settings_obj.biometric_sensitivity = request.POST.get(
            "biometric_sensitivity", "Standard"
        )
        try:
            settings_obj.auto_abort_timeout = int(
                request.POST.get("auto_abort_timeout", 10)
            )
        except (ValueError, TypeError):
            settings_obj.auto_abort_timeout = 10

        settings_obj.email_notifications = (
            request.POST.get("email_notifications") == "on"
        )
        settings_obj.telemetry_sharing = request.POST.get("telemetry_sharing") == "on"
        settings_obj.save()

        messages.success(request, "System Neural Configuration Saved.")
        return redirect("user_settings:settings")

    return render(request, "user_settings/settings.html", {"settings": settings_obj})
