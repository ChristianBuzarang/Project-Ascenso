from django.contrib import admin
from .models import AscensionRecord, FearScenario, UserDevice


@admin.register(AscensionRecord)
class AscensionRecordAdmin(admin.ModelAdmin):
    # This dictates what columns the Admin sees in the database viewer
    list_display = ("user", "scenario", "target_level", "peak_hr", "timestamp")

    # Adds a filter box on the right side to quickly sort data
    list_filter = ("target_level", "timestamp")

    # Adds a search bar at the top
    search_fields = ("user__username", "scenario_name")


@admin.register(FearScenario)
class FearScenarioAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_active", "created_by")
    list_filter = ("category", "is_active")
    search_fields = ("name", "category")


@admin.register(UserDevice)
class UserDeviceAdmin(admin.ModelAdmin):
    list_display = ("device_name", "user", "mac_address", "is_active")
