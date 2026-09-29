import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from apps.simulation.models import (
    AscensionRecord,
)  # Cross-import allowed for data fetching

FEAR_SCENARIOS = {
    "darkness": {"name": "[Primal] Fear of Darkness"},
    "spiders": {"name": "[Primal] Fear of Spiders"},
    "public_speaking": {"name": "[Social] Public Speaking"},
    "unknown": {"name": "[Existential] The Unknown"},
}
FEAR_LEVELS = {
    "1": "Level 1: Apprehension",
    "3": "Level 3: Fright",
    "5": "Level 5: Panic",
    "7": "Level 7: Collapse",
}


@login_required(login_url="login:login")
def home_view(request):
    records = AscensionRecord.objects.filter(user=request.user).order_by("timestamp")
    labels, peak_hrs, end_hrs = [], [], []
    for i, record in enumerate(records):
        labels.append(f"Session {i + 1}")
        peak_hrs.append(record.peak_hr)
        end_hrs.append(record.end_hr)

    context = {
        "scenarios": FEAR_SCENARIOS,
        "levels": FEAR_LEVELS,
        "has_history": len(records) > 0,
        "chart_labels": json.dumps(labels),
        "chart_peak_hr": json.dumps(peak_hrs),
        "chart_end_hr": json.dumps(end_hrs),
    }
    return render(request, "home/home.html", context)


@login_required(login_url="login:login")
def chart_data_api(request):
    """Silent API endpoint that fetches the Supabase data in the background"""
    records = AscensionRecord.objects.filter(user=request.user).order_by("timestamp")

    labels = []
    peak_hrs = []
    end_hrs = []

    for i, record in enumerate(records):
        labels.append(f"Session {i + 1}")
        peak_hrs.append(record.peak_hr)
        end_hrs.append(record.end_hr)

    return JsonResponse(
        {
            "has_history": len(records) > 0,
            "chart_labels": labels,
            "chart_peak_hr": peak_hrs,
            "chart_end_hr": end_hrs,
        }
    )
