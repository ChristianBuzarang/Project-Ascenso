from django.contrib import admin
from .models import AscensionRecord


@admin.register(AscensionRecord)
class AscensionRecordAdmin(admin.ModelAdmin):
    # This dictates what columns the Admin sees in the database viewer
    list_display = (
        "user",
        "anonymized_id",
        "scenario",
        "target_level",
        "peak_hr",
        "timestamp",
    )

    # Adds a filter box on the right side to quickly sort data
    list_filter = ("scenario", "target_level", "timestamp")

    # Adds a search bar at the top
    search_fields = ("user__username", "anonymized_id", "scenario")
